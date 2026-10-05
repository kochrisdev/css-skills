"""Read-only audit of source; all mutation probes use disposable local copies."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, shutil, sys, subprocess, argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root', required=True, type=Path, help='Existing CSS v0.6 source checkout; never modified')
parser.add_argument('--output', type=Path, help='Optional explicit output JSON path')
args=parser.parse_args()
ROOT=args.root.resolve()
if not (ROOT/'catalog/skill-registry.json').is_file():
    parser.error('root must be an existing CSS source checkout')
sys.path.insert(0,str(ROOT))
from css.core import Catalog, content_digest
from css.install import install
records=[]
def record(name, **values):
    records.append({'probe':name,**values})
def copied(folder):
    p=Path(folder)/'copy'
    shutil.copytree(ROOT,p,ignore=shutil.ignore_patterns('.git','__pycache__'))
    return p
def save(p,obj):p.write_text(json.dumps(obj,indent=2),encoding='utf-8')
# Test deletion lifecycle using an inert text fixture, not a runnable helper.
with TemporaryDirectory() as t:
    src=copied(t); target=Path(t)/'target'; target.mkdir()
    fixture=src/'skills/analyzing-requirements/references/retired-audit-fixture.txt'
    fixture.write_text('Retired resource; inert audit fixture.',encoding='utf-8')
    def refresh():
        p=src/'catalog/skill-registry.json';reg=json.loads(p.read_text())
        next(s for s in reg['skills'] if s['name']=='analyzing-requirements')['content_sha256']=content_digest(src,'skills/analyzing-requirements')
        save(p,reg)
    refresh();install(Catalog(src),'starter',target,apply=True)
    fixture.unlink();refresh();c=Catalog(src);valid=c.validate()['ok'];res=install(c,'starter',target,apply=True)
    retired=target/'.claude/skills/analyzing-requirements/references/retired-audit-fixture.txt'
    record('managed_resource_removed_upstream',source_valid=valid,upstream_file_exists=fixture.exists(),installed_file_retained=retired.exists(),deletion_in_plan=any(x['action']=='delete' for x in res['plan']))
# Runtime declares all PE steps human-reviewed, but only high-risk annotations are validated.
with TemporaryDirectory() as t:
    src=copied(t);p=src/'workflows/pe-underwriting.json';v=json.loads(p.read_text());v['steps'][0].pop('approval');save(p,v)
    result=Catalog(src).validate()
    record('medium_risk_pe_gate_removed',validation_ok=result['ok'],errors=[i for i in result['issues'] if i['severity']=='error'])
# Invalid shapes should produce structured errors; capture current exceptions without changing source.
for name,path,value in [
    ('profile_nonobject','profiles/starter.json',[]),
    ('workflow_nonobject_step','workflows/pe-underwriting.json',None),
]:
    with TemporaryDirectory() as t:
        src=copied(t);p=src/path
        if value is None:
            value=json.loads(p.read_text());value['steps'][0]=None
        save(p,value)
        run=subprocess.run([sys.executable,'-m','css','--root',str(src),'validate'],cwd=ROOT,text=True,capture_output=True)
        record(name,exit_code=run.returncode,raw_traceback='Traceback (most recent call last)' in run.stderr,stderr_tail=run.stderr.strip().splitlines()[-2:])
# Valid-looking self-declared evidence with an ambiguous duplicate status key.
with TemporaryDirectory() as t:
    p=Path(t)/'ambiguous-evidence.json'
    p.write_text('{"candidate_digest":"fixture","environment":"sandbox","required_checks":["tests"],"checks":[{"name":"tests","status":"fail","status":"pass","candidate_digest":"fixture","environment":"sandbox","observed_at":"2026-10-05T00:00:00Z","evidence_ref":"synthetic://test"}]}')
    run=subprocess.run([sys.executable,str(ROOT/'skills/gating-releases/scripts/check_evidence.py'),str(p),'--now','2026-10-05T00:01:00Z'],text=True,capture_output=True)
    record('duplicate_json_evidence_status',exit_code=run.returncode,output=json.loads(run.stdout),limitation='Synthetic shape checker only; this is not an observed production authorization bypass.')
with TemporaryDirectory() as t:
    p=Path(t)/'ambiguous-ledger.json'
    tx={'id':'tx','idempotency_key':'k','entries':[{'entity':'e','currency':'USD','account':'cash','amount_minor':100,'side':'debit'},{'entity':'e','currency':'USD','account':'sales','amount_minor':100,'side':'credit'}]}
    text=json.dumps({'transactions':[tx]}).replace('"amount_minor": 100','"amount_minor": 999, "amount_minor": 100',1)
    p.write_text(text)
    run=subprocess.run([sys.executable,str(ROOT/'skills/designing-ledgers/scripts/check_ledger.py'),str(p)],text=True,capture_output=True)
    record('duplicate_json_ledger_amount',exit_code=run.returncode,output=json.loads(run.stdout))
# New, independently authored (but not a held-out production benchmark) discovery queries.
c=Catalog(ROOT)
queries=[
 ('Can we buy this manufacturer without relying on a higher exit valuation?','screening-buyouts'),
 ('Build a 100-day post-acquisition operating plan.','planning-pe-value-creation'),
 ('Assess recurring earnings adjustments and cash conversion before acquiring a business.','conducting-quality-of-earnings'),
 ('What proportion will founders own after a primary financing round?','modeling-venture-cap-tables'),
 ('Assess distribution proceeds after debt repayment and transaction expenses.','modeling-buyouts'),
 ('Find a guide for reconciling payouts when bank records disagree with provider statements.','designing-reconciliation'),
 ('Turn our vague product idea into measurable acceptance requirements.','analyzing-requirements'),
 ('Evaluate whether a proposed bank replica can safely simulate liquidity shortfalls.','designing-bank-digital-twins'),
 ('Our application intermittently writes the same payment twice. Diagnose the defect.','debugging-code'),
 ('Check an AI assistant can resist hidden instructions in retrieved documents.','testing-agents'),
 ('Prepare an investor committee decision paper including reasons not to invest.','preparing-investment-committee-memos'),
 ('Evaluate a manager before committing as a limited partner to the next fund.','diligencing-fund-managers'),
 ('Review conflicting technical papers and explain their limitations.','conducting-research'),
 ('What is the weather in Tokyo tomorrow?',None),
 ('Teach a child how plants use sunlight.',None),
 ('Write a science fiction story about a lost space station.',None),
 ('Give me a recipe for a vegetable curry.',None),
]
routing=[]
for query,expected in queries:
    result=c.search(query,3);actual=[s['name'] for s in result['results']]
    routing.append({'query':query,'expected':expected,'actual':actual,'pass':(not actual if expected is None else expected in actual)})
report={'scope':'Synthetic local audit probes; source and GitHub unchanged. No live model testing or authenticated financial actions.','probes':records,'exploratory_routing':routing,'routing_note':'Small reviewer-authored probes; not an estimate of real-world routing accuracy.'}
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    save(args.output,report)
print(json.dumps(report,indent=2))
