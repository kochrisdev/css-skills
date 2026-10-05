"""Narrow, offline PE/VC arithmetic on declared synthetic inputs.

No legal interpretation, financing execution, valuation certification or investment
recommendation. Decimal strings are accepted; binary floats and booleans are rejected.
The caller must reconcile source scope, dates, currency and gross/net basis.
"""
from __future__ import annotations
import argparse
from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
import json
from pathlib import Path
import re
import sys
from typing import Any
from .core import CSSError, read_json

Number = str | int | Decimal

def amount(value: Number, label: str, *, positive: bool = False) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise CSSError(f'{label}: use an exact decimal string or integer, not float/bool')
    text = str(value)
    if len(text) > 100 or not re.fullmatch(r'\d+(?:\.\d{1,12})?', text):
        raise CSSError(f'{label}: expected a nonnegative ordinary decimal with at most 12 fractional digits')
    try:
        result = Decimal(text)
    except InvalidOperation as exc:
        raise CSSError(f'{label}: invalid decimal') from exc
    if not result.is_finite() or (positive and result <= 0):
        raise CSSError(f'{label}: expected a finite positive amount')
    return result

def unit(currency: str) -> str:
    if not isinstance(currency, str) or not re.fullmatch('[A-Z]{3}', currency):
        raise CSSError('currency must be a declared three-letter uppercase code; no FX conversion is performed')
    return currency

def fmt(value: Decimal) -> str:
    text = format(value, 'f')
    return text.rstrip('0').rstrip('.') if '.' in text else text

def fund_multiples(*, paid_in: Number, distributions: Number, nav: Number,
                   currency: str, as_of: str, basis: str) -> dict[str, Any]:
    unit(currency)
    if basis not in {'gross', 'net'}:
        raise CSSError('basis must be explicitly gross or net; no automatic conversion')
    if not isinstance(as_of, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', as_of):
        raise CSSError('as_of must be YYYY-MM-DD')
    try:
        date.fromisoformat(as_of)
    except ValueError as exc:
        raise CSSError('as_of is not a valid calendar date') from exc
    p = amount(paid_in, 'paid_in', positive=True)
    d, n = amount(distributions, 'distributions'), amount(nav, 'nav')
    with localcontext() as c:
        c.prec = 120
        result = {'DPI': fmt(d/p), 'RVPI': fmt(n/p), 'TVPI': fmt((d+n)/p)}
    return {**result, 'currency':currency, 'as_of':as_of, 'basis':basis,
            'notice':'Simple positive-paid-in, nonnegative-value scope only. Matched source scope and basis are asserted by the caller, not verified. No IRR, carry, fees, recallability or FX treatment is computed.'}

def priced_round(*, pre_money: Number, investment: Number, holders: dict[str, Number],
                 currency: str) -> dict[str, Any]:
    unit(currency)
    if not isinstance(holders, dict) or not holders:
        raise CSSError('holders must be a nonempty name-to-fully-diluted-shares mapping')
    if any(not isinstance(k, str) or not k.strip() or k == 'new-investor' for k in holders):
        raise CSSError('holder names must be nonblank; new-investor is reserved')
    shares = {k: amount(v, k) for k,v in holders.items()}
    pre, cash = amount(pre_money,'pre_money',positive=True), amount(investment,'investment',positive=True)
    with localcontext() as c:
        c.prec = 120
        total = sum(shares.values(), Decimal(0))
        if total <= 0: raise CSSError('fully diluted shares must total more than zero')
        new = cash * total / pre
        price = pre / total
        post = total + new
        rows = {k:{'shares':fmt(v),'ownership_fraction':fmt(v/post)} for k,v in shares.items()}
        rows['new-investor']={'shares':fmt(new),'ownership_fraction':fmt(new/post)}
        return {'currency':currency,'price_per_share':fmt(price),'post_money':fmt(pre+cash),
                'post_round_shares':fmt(post),'holders':rows,
                'notice':'Simple primary priced round only. Existing fully diluted denominator is supplied; no SAFE/note conversion, pool increase, secondary sale, rights or liquidation preferences. Fractional shares are mathematical, not legal issuance.'}

def sources_uses(*, sources: dict[str, Number], uses: dict[str, Number], currency: str) -> dict[str, Any]:
    unit(currency)
    for label, mapping in [('sources',sources),('uses',uses)]:
        if not isinstance(mapping,dict) or not mapping or any(not isinstance(k,str) or not k.strip() for k in mapping):
            raise CSSError(f'{label} must be a nonempty named amount mapping')
    with localcontext() as c:
        c.prec = 120
        s = sum((amount(v,k) for k,v in sources.items()),Decimal(0))
        u = sum((amount(v,k) for k,v in uses.items()),Decimal(0))
        return {'currency':currency,'sources':fmt(s),'uses':fmt(u),'gap_sources_less_uses':fmt(s-u),
                'balanced':s==u,'notice':'Arithmetic reconciliation only; amount classifications and funding commitments are not verified.'}

def exit_bridge(*, enterprise_value: Number, debt: Number, cash: Number, costs: Number,
                invested_equity: Number, interim_distributions: Number, currency: str) -> dict[str, Any]:
    unit(currency)
    ev,d,cost,cash_d = (amount(enterprise_value,'enterprise_value'),amount(debt,'debt'),amount(costs,'costs'),amount(cash,'cash'))
    p = amount(invested_equity,'invested_equity',positive=True)
    interim = amount(interim_distributions,'interim_distributions')
    with localcontext() as c:
        c.prec = 120
        residual = ev + cash_d - d - cost
        equity = max(Decimal(0),residual)
        return {'currency':currency,'residual_before_floor':fmt(residual),'terminal_equity':fmt(equity),
                'claim_shortfall':fmt(max(Decimal(0),-residual)),'MOIC':fmt((equity+interim)/p),
                'notice':'Single-equity-class terminal bridge only; no preference waterfall, taxes, debt schedule, IRR or legal distribution priority. Invested equity must include all contributions; interim receipts must not be double-counted in exit cash.'}

OPERATIONS = {'fund-multiples':fund_multiples,'priced-round':priced_round,'sources-uses':sources_uses,'exit-bridge':exit_bridge}

def main(argv: list[str] | None = None) -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path,help='JSON with operation and inputs; synthetic or authorized data only')
    args=parser.parse_args(argv)
    try:
        payload=read_json(args.input)
        if not isinstance(payload,dict) or set(payload)!={'operation','inputs'}:
            raise CSSError('expected exactly operation and inputs')
        if not isinstance(payload['operation'],str) or payload['operation'] not in OPERATIONS or not isinstance(payload['inputs'],dict):
            raise CSSError('unknown operation or invalid inputs')
        output=OPERATIONS[payload['operation']](**payload['inputs'])
        print(json.dumps(output,indent=2))
        return 0 if output.get('balanced',True) else 1
    except (CSSError,TypeError,InvalidOperation,ValueError) as exc:
        print(json.dumps({'error':str(exc)}),file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
