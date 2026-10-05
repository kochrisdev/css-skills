"""Local-only CLI. All machine output is JSON; operations are explicit."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
from . import __version__
from .core import Catalog, CSSError, read_json
from .install import install, restore
from .doctor import diagnose

def main(argv: list[str] | None = None) -> int:
    p=argparse.ArgumentParser(prog='python -m css',description='CSS catalog tools; never executes business workflows.')
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1],help='CSS source checkout')
    p.add_argument('--version',action='version',version=__version__)
    sub=p.add_subparsers(dest='command',required=True)
    v=sub.add_parser('validate',help='Check structure, integrity and contracts; not model behavior')
    v.add_argument('--release',action='store_true',help='Also require unresolved release-readiness conditions to be cleared')
    sub.add_parser('inventory',help='Summarize catalog and maturity')
    sub.add_parser('graph',help='Derive related-skill and artifact dependency graph from canonical data')
    d=sub.add_parser('doctor',help='Read-only check of Python and local Git folder')
    d.add_argument('--project',type=Path,default=Path.cwd())
    for name in ['search','route']:
        s=sub.add_parser(name,help='Explainable lexical retrieval; no autonomous actions')
        s.add_argument('query');s.add_argument('--limit',type=int,default=5)
        s.add_argument('--include-drafts',action='store_true')
    s=sub.add_parser('plan',help='Validate and show a declared workflow, without running it')
    s.add_argument('workflow')
    s=sub.add_parser('install',help='Preview skill installation; --apply performs local file writes')
    s.add_argument('--profile',default='starter');s.add_argument('--target',required=True,type=Path)
    s.add_argument('--runtime',choices=['claude','codex','generic'],default='claude')
    s.add_argument('--apply',action='store_true')
    s=sub.add_parser('restore',help='Preview backup restoration; --apply restores managed files')
    s.add_argument('--target',required=True,type=Path);s.add_argument('--backup',required=True)
    s.add_argument('--apply',action='store_true')
    sub.add_parser('benchmark-routing',help='Run the bundled lexical retrieval smoke cases, not an LLM benchmark')
    args=p.parse_args(argv)
    try:
        if args.command=='doctor':
            result=diagnose(args.project)
        elif args.command=='restore':
            result=restore(args.target,args.backup,args.apply)
        else:
            c=Catalog(args.root)
            if args.command=='validate':
                result=c.validate()
                if args.release:
                    result['release_ready']=False
                    result['ok']=False
                    result['release_blockers']=['Owner must resolve inherited license ambiguity','Independent domain review and target-runtime behavior evaluation are not recorded']
            elif args.command=='inventory':
                result={'version':c.raw['version'],'skills':len(c.skills),'status':dict(Counter(s['status'] for s in c.skills)),
                        'domains':dict(sorted(Counter(s['domain'] for s in c.skills).items())),
                        'behavioral_evaluation':'not_run','license_status':'owner_confirmation_required'}
            elif args.command=='graph':
                result={'nodes':[{'id':s['id'],'name':s['name'],'status':s['status']} for s in c.skills],
                        'edges':[{'source':s['name'],'target':n,'kind':'related-not-execution-dependency'} for s in c.skills for n in s['related_skills']],
                        'workflows':[c.workflow(p.stem) for p in sorted((c.root/'workflows').glob('*.json'))],
                        'notice':'Derived on demand. Related edges do not force execution; workflow bindings define actual ordering.'}
            elif args.command in ('search','route'):
                result=c.search(args.query,args.limit,args.include_drafts)
            elif args.command=='plan':result=c.workflow(args.workflow)
            elif args.command=='install':result=install(c,args.profile,args.target,args.runtime,args.apply)
            elif args.command=='benchmark-routing':
                cases=read_json(c.root/'evals/routing-smoke.json')['cases'];records=[]
                for case in cases:
                    r=c.search(case['query'],case.get('k',3))
                    actual=[s['name'] for s in r['results']]
                    passed=(not actual if case['expected'] is None else case['expected'] in actual)
                    records.append({'id':case['id'],'query':case['query'],'expected':case['expected'],'actual':actual,'pass':passed})
                result={'scope':'authored lexical retrieval smoke cases; no held-out performance claim and no model evaluation',
                        'cases':records,'passed':sum(x['pass'] for x in records),'total':len(records),'ok':all(x['pass'] for x in records)}
            else:raise CSSError('unsupported command')
        print(json.dumps(result,indent=2,ensure_ascii=False))
        if result.get('ok') is False or result.get('conflicts'):return 1
        return 0
    except (CSSError,OSError,UnicodeError,KeyError,TypeError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__=='__main__':raise SystemExit(main())
