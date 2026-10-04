from pathlib import Path
import json,sys
r=Path(__file__).resolve().parents[1]; reg=json.load(open(r/'catalog/skill-registry.json')); e=[]; names=[s['name'] for s in reg['skills']]
if len(names)!=200:e.append(f'expected 200 skills, got {len(names)}')
if len(names)!=len(set(names)):e.append('duplicate names')
req=['## Purpose','## Use when','## Do not use when','## Inputs','## Workflow','## Output contract','## Quality gates','## Failure handling','## Safety and permissions']
N=set(names)
for s in reg['skills']:
 p=r/s['path']
 if not p.exists():e.append('missing '+s['name']);continue
 t=p.read_text()
 for h in req:
  if h not in t:e.append(s['name']+' missing '+h)
 for d in s.get('depends_on',[]):
  if d not in N:e.append(s['name']+' bad dependency '+d)
 if not (r/'evals/scenarios'/(s['name']+'.md')).exists():e.append(s['name']+' missing eval')
if e: print('\n'.join(e));sys.exit(1)
print(f'PASS: {len(names)} skills conform to CSS v0.4 structural checks.')
