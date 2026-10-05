"""Synthetic journal validation only. No posting, network access or financial advice."""
from __future__ import annotations
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys
from typing import Any

def check(document: dict[str,Any]) -> list[str]:
    errors=[];ids=set();keys=set()
    if not isinstance(document,dict) or not isinstance(document.get('transactions'),list) or not document['transactions']:
        return ['transactions must be a nonempty array']
    for i,tx in enumerate(document['transactions']):
        label=f'transaction[{i}]'
        if not isinstance(tx,dict):errors.append(label+' must be an object');continue
        tid=tx.get('id');key=tx.get('idempotency_key')
        if not isinstance(tid,str) or not tid or tid in ids:errors.append(label+' invalid or duplicate transaction id')
        else:ids.add(tid)
        if not isinstance(key,str) or not key or key in keys:errors.append(label+' invalid or duplicate idempotency key')
        else:keys.add(key)
        entries=tx.get('entries')
        if not isinstance(entries,list) or len(entries)<2:errors.append(label+' requires at least two entries');continue
        totals=defaultdict(int)
        for j,e in enumerate(entries):
            if not isinstance(e,dict):errors.append(f'{label}[{j}] must be an object');continue
            if any(not isinstance(e.get(k),str) or not e[k] for k in ('entity','currency','account')):
                errors.append(f'{label}[{j}] requires entity, currency and account');continue
            currency=e['currency']
            if len(currency)!=3 or not currency.isascii() or not currency.isalpha() or not currency.isupper():
                errors.append(f'{label}[{j}] invalid currency code syntax');continue
            amount=e.get('amount_minor');side=e.get('side')
            if type(amount) is not int or amount<=0:
                errors.append(f'{label}[{j}] amount_minor must be a positive integer');continue
            if side not in ('debit','credit'):
                errors.append(f'{label}[{j}] side must be debit or credit');continue
            totals[(e['entity'],currency)]+=amount if side=='debit' else -amount
        for (entity,currency),balance in totals.items():
            if balance!=0:errors.append(f'{label} unbalanced {entity}/{currency}: {balance}')
    return errors

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:errors=check(json.loads(a.input.read_text(encoding='utf-8')))
    except (OSError,json.JSONDecodeError) as exc:errors=[str(exc)]
    print(json.dumps({'ok':not errors,'errors':errors,'scope':'synthetic shape, uniqueness and balance checks; not accounting correctness or live posting'}))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
