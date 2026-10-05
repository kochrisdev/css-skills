"""Check declared evidence binding/freshness; cannot authenticate evidence or approvals."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
from typing import Any

def parse(value: str) -> datetime:
    if not isinstance(value,str):raise ValueError('timestamp must be a string')
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    if dt.tzinfo is None:raise ValueError('timestamp requires timezone')
    return dt.astimezone(timezone.utc)

def check(record: dict[str,Any], *, now: datetime, max_age_hours: float=24) -> list[str]:
    errors=[]
    if now.tzinfo is None:return ['now must include timezone']
    if not math.isfinite(max_age_hours) or max_age_hours<=0:return ['max age must be finite and positive']
    if not isinstance(record,dict):return ['record must be an object']
    candidate=record.get('candidate_digest');environment=record.get('environment')
    if not isinstance(candidate,str) or not candidate or not isinstance(environment,str) or not environment:
        return ['candidate_digest and environment are required']
    required=record.get('required_checks')
    if not isinstance(required,list) or not required or any(not isinstance(x,str) or not x for x in required) or len(set(required))!=len(required):
        return ['required_checks must be a nonempty array of unique names']
    seen=set()
    checks=record.get('checks')
    if not isinstance(checks,list):return ['checks must be an array']
    for check in checks:
        if not isinstance(check,dict):errors.append('check must be an object');continue
        name=check.get('name')
        if not isinstance(name,str) or not name:errors.append('check name required');continue
        if name in seen:errors.append('duplicate check '+name)
        seen.add(name)
        if check.get('candidate_digest')!=candidate:errors.append(name+': candidate mismatch')
        if check.get('environment')!=environment:errors.append(name+': environment mismatch')
        if name in required and check.get('status')!='pass':errors.append(name+': mandatory check is not pass')
        if not isinstance(check.get('evidence_ref'),str) or not check['evidence_ref']:errors.append(name+': missing evidence reference')
        try:
            age=(now-parse(check['observed_at'])).total_seconds()/3600
            if age<0 or age>max_age_hours:errors.append(name+': future or stale evidence')
        except (KeyError,TypeError,ValueError):errors.append(name+': invalid observation timestamp')
    for name in set(required)-seen:errors.append('missing required check '+name)
    return errors

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path)
    p.add_argument('--now',help='Explicit ISO-8601 time for reproducible fixture tests')
    p.add_argument('--max-age-hours',type=float,default=24);a=p.parse_args()
    try:
        errors=check(json.loads(a.input.read_text(encoding='utf-8')),now=parse(a.now) if a.now else datetime.now(timezone.utc),max_age_hours=a.max_age_hours)
    except (OSError,json.JSONDecodeError,ValueError) as exc:errors=[str(exc)]
    print(json.dumps({'ok':not errors,'errors':errors,'scope':'declared bindings and freshness only; evidence authenticity and human authorization NOT verified'}))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
