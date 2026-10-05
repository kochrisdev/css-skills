"""Dependency-free registry validation, explicit artifact planning and lexical discovery."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, asdict
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
from typing import Any

class CSSError(ValueError):
    """An actionable validation or precondition failure."""

SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
FIELDS = {'name', 'description'}
SECTIONS = ['Purpose', 'Use when', 'Do not use when', 'Inputs', 'Workflow',
            'Output contract', 'Quality gates', 'Failure handling', 'Safety and permissions']
STOP = set('a an the and or for to of in on is are be as by it this that with from into use using skill skills design designing review reviewing create creating analyze analyzing provide capability governed scope evidence explicit request task please help'.split())
ALIASES = {'reconcile':'reconciliation','reconciling':'reconciliation','ledgers':'ledger',
           'payments':'payment','payouts':'payout','agents':'agent','twin':'twin','twins':'twin',
           'requirements':'requirement','tests':'test','testing':'test','tested':'test',
           'debugging':'debug','debugger':'debug','deploying':'deploy','deployment':'deploy',
           'evaluations':'evaluation','evaluating':'evaluation','llms':'llm',
           'wallets':'wallet','guardrails':'guardrail','incidents':'incident','releases':'release','permissions':'permission','controls':'control','tools':'tool','datasets':'dataset'}

def read_json(path: Path) -> Any:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in pairs:
            if key in result:
                raise CSSError(f'duplicate JSON key: {key} in {path}')
            result[key] = value
        return result
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CSSError(f'cannot read JSON {path}: {exc}') from exc

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def confined(root: Path, relative: str) -> Path:
    """Validate an untrusted POSIX relative path, including symlink components."""
    if not isinstance(relative, str) or not relative or '\\' in relative or ':' in relative:
        raise CSSError(f'unsafe relative path: {relative!r}')
    p = PurePosixPath(relative)
    if p.is_absolute() or '..' in p.parts or '.' in relative.split('/') or '' in relative.split('/'):
        raise CSSError(f'unsafe relative path: {relative!r}')
    root = root.absolute()
    for parent in [root, *root.parents]:
        if parent.is_symlink():
            raise CSSError(f'symlink parent is not supported: {parent}')
    out = root.joinpath(*p.parts)
    for part in [out, *out.parents]:
        if part == root.parent:
            break
        if part.is_symlink():
            raise CSSError(f'symlink is not supported: {part}')
    if not out.resolve().is_relative_to(root.resolve()):
        raise CSSError(f'path escapes root: {relative}')
    return out

def frontmatter(text: str) -> tuple[dict[str, str], str]:
    """CSS canonical YAML subset: two single-line JSON strings or plain slugs.

    This intentionally rejects YAML extensions, aliases and multiline scalars.
    It is not advertised as a general YAML parser.
    """
    if not text.startswith('---\n'):
        raise CSSError('frontmatter must begin at the first byte with --- and LF')
    parts = text.split('\n---\n', 1)
    if len(parts) != 2:
        raise CSSError('unterminated frontmatter')
    result = {}
    for line in parts[0][4:].splitlines():
        if ':' not in line:
            raise CSSError('frontmatter requires key: value lines')
        key, raw = line.split(':', 1)
        raw = raw.strip()
        if key not in FIELDS or key in result:
            raise CSSError(f'unsupported or duplicate frontmatter field: {key}')
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise CSSError('invalid quoted frontmatter scalar') from exc
        elif SLUG.fullmatch(raw):
            value = raw
        else:
            raise CSSError('canonical scalar must be a JSON string or slug')
        if not isinstance(value, str) or not value.strip():
            raise CSSError(f'frontmatter {key} must be a nonempty string')
        result[key] = value
    if set(result) != FIELDS:
        raise CSSError('name and description are required')
    return result, parts[1]

def tree_files(root: Path, subdir: str) -> dict[str, bytes]:
    root = root.absolute()
    base = confined(root, subdir)
    if not base.is_dir():
        raise CSSError(f'missing directory: {subdir}')
    result = {}
    for p in sorted(base.rglob('*')):
        if '__pycache__' in p.parts:
            continue
        confined(root, p.relative_to(root).as_posix())
        if p.is_file():
            result[p.relative_to(base).as_posix()] = p.read_bytes()
    return result

def content_digest(root: Path, subdir: str) -> str:
    manifest = {p: digest(b) for p,b in tree_files(root, subdir).items()}
    return digest(json.dumps(manifest, sort_keys=True, separators=(',', ':')).encode())

def topo(nodes: dict[str, list[str]]) -> list[str]:
    ordered, state = [], {}
    def visit(node: str, stack: list[str]) -> None:
        if node not in nodes:
            raise CSSError(f'unknown dependency: {node}')
        if state.get(node) == 1:
            raise CSSError('dependency cycle: ' + ' -> '.join(stack + [node]))
        if state.get(node) == 2:
            return
        state[node] = 1
        for dep in nodes[node]:
            visit(dep, stack + [node])
        state[node] = 2
        ordered.append(node)
    for node in sorted(nodes):
        visit(node, [])
    return ordered

@dataclass
class Issue:
    severity: str
    code: str
    path: str
    message: str

class Catalog:
    def __init__(self, root: Path):
        self.root = root.absolute()
        self.raw = read_json(confined(self.root, 'catalog/skill-registry.json'))
        if not isinstance(self.raw, dict) or not isinstance(self.raw.get('skills'), list):
            raise CSSError('registry must contain a skills array')
        self.skills = self.raw['skills']
        if any(not isinstance(s, dict) or not isinstance(s.get('name'), str) for s in self.skills):
            raise CSSError('every registry entry requires a string name')
        self.by_name = {s['name']: s for s in self.skills}

    def validate(self, integrity: bool = True) -> dict[str, Any]:
        issues: list[Issue] = []
        def add(sev: str, code: str, path: str, message: str) -> None:
            issues.append(Issue(sev, code, path, message))
        if self.raw.get('schema_version') != '1.0':
            add('error','SCHEMA','catalog/skill-registry.json','unsupported schema_version')
        for key in ('name','id'):
            vals = [s.get(key) for s in self.skills]
            if len(vals) != len(set(str(v) for v in vals)):
                add('error','DUPLICATE','catalog/skill-registry.json',f'duplicate {key}')
        workflows = Counter()
        pilot_workflows = Counter()
        domains = {d['id'] for d in self.raw.get('domains',[]) if isinstance(d,dict) and 'id' in d}
        for s in self.skills:
            name = s['name']; path = s.get('path', '')
            try:
                expected_fields = {'id','name','domain','risk','version','path','legacy_path','status','maturity','description','inputs','outputs','keywords','depends_on','related_skills','behavioral_evaluation','human_review','content_sha256'}
                if set(s) != expected_fields:
                    raise CSSError('registry entry has missing or unknown fields')
                if s.get('version') != self.raw.get('version') or s.get('human_review') != 'not_recorded':
                    raise CSSError('invalid version or unsupported human-review claim')
                if not isinstance(s.get('content_sha256'),str) or not re.fullmatch('[0-9a-f]{64}',s['content_sha256']):
                    raise CSSError('invalid content digest')
                if not SLUG.fullmatch(name) or len(name)>64:
                    raise CSSError('invalid skill name')
                if not re.fullmatch(r'CSS-\d{3}', s.get('id','')):
                    raise CSSError('invalid canonical ID')
                if s.get('domain') not in domains:
                    raise CSSError('unknown domain')
                if s.get('status') not in ('draft','pilot'):
                    raise CSSError('status requires draft or pilot; validated is not supported without a release-policy revision')
                if s.get('maturity') != ('procedural' if s['status']=='pilot' else 'instruction'):
                    raise CSSError('maturity inconsistent with status')
                if s.get('behavioral_evaluation') != 'not_run':
                    raise CSSError('behavioral promotion requires a separately reviewed evidence policy')
                if s.get('risk') not in ('low','medium','high'):
                    raise CSSError('unknown risk')
                if path != f'skills/{name}/SKILL.md':
                    raise CSSError('path does not match canonical skill name')
                for field in ('inputs','outputs','keywords','depends_on','related_skills'):
                    if not isinstance(s.get(field),list) or any(not isinstance(x,str) or not x for x in s[field]):
                        raise CSSError(f'{field} must be an array of nonempty strings')
                    if len(set(s[field])) != len(s[field]):
                        raise CSSError(f'{field} must not contain duplicates')
                for related in s['related_skills']:
                    if related not in self.by_name:
                        raise CSSError(f'unknown related skill: {related}')
                text = confined(self.root,path).read_text(encoding='utf-8')
                fm, body = frontmatter(text)
                if fm['name'] != name or fm['description'] != s.get('description'):
                    raise CSSError('frontmatter disagrees with registry')
                if len(fm['description'])>1024:
                    raise CSSError('description exceeds 1024 characters')
                for heading in SECTIONS:
                    if f'## {heading}\n' not in body:
                        raise CSSError(f'missing section: {heading}')
                if len(text.splitlines())>500:
                    raise CSSError('SKILL.md exceeds CSS 500-line budget')
                subdir = f'skills/{name}'
                for rel in re.findall(r'\]\(([^)]+)\)',body):
                    if re.match(r'https?://',rel) or rel.startswith('#'):
                        continue
                    link = confined(self.root, f'{subdir}/{rel.split("#")[0]}')
                    if not link.is_file():
                        raise CSSError(f'missing linked resource: {rel}')
                if integrity and content_digest(self.root,subdir) != s.get('content_sha256'):
                    raise CSSError('content integrity mismatch; review and regenerate intentionally')
                workflow = re.search(r'## Workflow\n(.*?)(?=\n## |\Z)',body,re.S)
                workflows[workflow.group(1).strip() if workflow else ''] += 1
                if s['status']=='pilot':
                    pilot_workflows[workflow.group(1).strip() if workflow else ''] += 1
                    for rel in ['references/checklist.md','templates/output.md','evals/cases.json']:
                        if not confined(self.root,f'{subdir}/{rel}').is_file():
                            raise CSSError(f'pilot missing {rel}')
                    cases = read_json(confined(self.root,f'{subdir}/evals/cases.json'))
                    if cases.get('skill') != name or cases.get('execution_status') != 'not_run':
                        raise CSSError('invalid behavioral case ownership or execution status')
                    kinds = set()
                    ids = set()
                    for case in cases.get('cases',[]):
                        if case.get('id') in ids:
                            raise CSSError('duplicate evaluation case ID')
                        ids.add(case.get('id')); kinds.add(case.get('kind'))
                        if len(case.get('prompt',''))<30 or not case.get('expected') or not case.get('forbidden'):
                            raise CSSError('behavioral cases require concrete prompt, expected and forbidden behaviors')
                    if not {'positive','negative','boundary','safety'} <= kinds:
                        raise CSSError('pilot requires positive, negative, boundary and safety cases')
            except (CSSError,OSError,UnicodeError,TypeError,ValueError) as exc:
                add('error','SKILL',path or name,str(exc))
        if any(count>1 for count in pilot_workflows.values()):
            add('error','DUPLICATE_PROCEDURE','skills','pilot skills must not have identical workflow bodies')
        actual = {p.parent.name for p in (self.root/'skills').glob('*/SKILL.md')}
        if actual != set(self.by_name):
            add('error','ORPHANS','skills','registry and skill directories disagree')
        try:
            topo({s['name']:s.get('depends_on',[]) for s in self.skills})
        except (CSSError,TypeError) as exc:
            add('error','GRAPH','catalog/skill-registry.json',str(exc))
        for p in sorted((self.root/'profiles').glob('*.json')):
            try:
                self.profile(p.stem)
            except (CSSError,TypeError,KeyError) as exc:
                add('error','PROFILE',str(p.relative_to(self.root)),str(exc))
        for p in sorted((self.root/'workflows').glob('*.json')):
            try:
                self.workflow(p.stem)
            except (CSSError,TypeError,KeyError) as exc:
                add('error','WORKFLOW',str(p.relative_to(self.root)),str(exc))
        drafts = sum(s.get('status')=='draft' for s in self.skills)
        if drafts:
            add('warning','DRAFTS','catalog/skill-registry.json',f'{drafts} legacy instruction drafts are not pilot procedures')
        add('warning','BEHAVIORAL','evals','live model behavior has not been measured in this release')
        if len((self.root/'LICENSE').read_text(encoding='utf-8'))<300:
            add('warning','LICENSE','LICENSE','incomplete inherited license notice; owner confirmation required before public release')
        return {'ok':not any(i.severity=='error' for i in issues),'skills':len(self.skills),
                'pilots':len(self.skills)-drafts,'drafts':drafts,
                'issues':[asdict(i) for i in issues],
                'scope':'structural, integrity, declared graphs and case-definition checks; NOT behavioral evaluation'}

    def profile(self, name: str, include_drafts: bool = False) -> list[str]:
        if not SLUG.fullmatch(name):
            raise CSSError('invalid profile name')
        p=read_json(confined(self.root,f'profiles/{name}.json'))
        if p.get('name') != name:
            raise CSSError('profile name does not match its filename')
        names=p.get('skills')
        if not isinstance(names,list) or not names or len(set(names))!=len(names):
            raise CSSError('profile requires unique skill names')
        expanded: set[str]=set()
        graph={s['name']:s.get('depends_on',[]) for s in self.skills}
        order=topo(graph)
        def add(n: str) -> None:
            if n not in self.by_name:
                raise CSSError(f'unknown skill: {n}')
            if n in expanded:return
            if self.by_name[n]['status']=='draft' and not include_drafts:
                raise CSSError(f'draft skill requires explicit opt-in: {n}')
            expanded.add(n)
            for dep in graph[n]:add(dep)
        for n in names:add(n)
        return [n for n in order if n in expanded]

    def workflow(self, name: str) -> dict[str, Any]:
        if not SLUG.fullmatch(name):
            raise CSSError('invalid workflow name')
        flow=read_json(confined(self.root,f'workflows/{name}.json'))
        if flow.get('name')!=name or not isinstance(flow.get('inputs'),dict):
            raise CSSError('workflow identity and input types are required')
        steps=flow.get('steps',[])
        if not isinstance(steps,list) or not steps:
            raise CSSError('workflow steps are required')
        ids=[s['id'] for s in steps]
        if len(set(ids))!=len(ids):raise CSSError('duplicate workflow step')
        by_id={s['id']:s for s in steps}
        order=topo({s['id']:s.get('after',[]) for s in steps})
        ancestors: dict[str,set[str]]={}
        produced: dict[str,tuple[str,str]]={}
        for sid in order:
            step=by_id[sid]; skill=self.by_name.get(step.get('skill'))
            if not skill or skill['status']!='pilot':raise CSSError(f'{sid}: workflow requires a pilot skill')
            ancestors[sid]=set(step.get('after',[]))
            for dep in step.get('after',[]):ancestors[sid] |= ancestors[dep]
            bindings=step.get('bindings',{})
            if set(bindings)!=set(skill['inputs']):raise CSSError(f'{sid}: input contract mismatch')
            for artifact_type,ref in bindings.items():
                if ref.startswith('input:'):
                    if flow['inputs'].get(ref[6:])!=artifact_type:raise CSSError(f'{sid}: missing or mistyped initial input {ref}')
                else:
                    if ref not in produced:raise CSSError(f'{sid}: missing artifact {ref}')
                    producer, actual_type=produced[ref]
                    if producer not in ancestors[sid] or actual_type!=artifact_type:
                        raise CSSError(f'{sid}: undeclared producer or artifact type mismatch: {ref}')
            if set(step.get('produces',{}).values())!=set(skill['outputs']):
                raise CSSError(f'{sid}: output contract mismatch')
            for output,artifact_type in step['produces'].items():
                if output in produced:raise CSSError(f'duplicate artifact: {output}')
                produced[output]=(sid,artifact_type)
            if skill['risk']=='high' and step.get('approval')!='human-review-required':
                raise CSSError(f'{sid}: high-risk step lacks human-review-required gate')
        return {**flow,'order':order,'status':'plan-only','executed':False,
                'notice':'Bindings validate declared types only. Input files, approval identity, freshness and execution are NOT verified.'}

    def search(self, query: str, limit: int = 5, include_drafts: bool = False) -> dict[str, Any]:
        if not 1<=limit<=50:raise CSSError('limit must be between 1 and 50')
        def tokens(value: str) -> list[str]:
            return [ALIASES.get(x,x) for x in re.findall('[a-z0-9]+',value.lower()) if x not in STOP]
        q=Counter(tokens(query)); pool=[s for s in self.skills if include_drafts or s['status']=='pilot']
        docs=[Counter(tokens(s['name'].replace('-',' ')+' '+s['description']+' '+' '.join(s['keywords'])*1)) for s in pool]
        df=Counter(t for d in docs for t in d)
        idf={t:math.log((1+len(docs))/(1+df[t]))+1 for t in df}
        results=[]
        for s,d in zip(pool,docs):
            shared=set(q)&set(d)
            if not shared:continue
            qweights={t:(1+math.log(n))*idf.get(t,math.log(1+len(docs))+1) for t,n in q.items()}
            dweights={t:(1+math.log(n))*idf[t] for t,n in d.items()}
            den=math.sqrt(sum(v*v for v in qweights.values())*sum(v*v for v in dweights.values()))
            score=sum(qweights[t]*dweights[t] for t in shared)/den if den else 0
            if score<0.12:continue
            results.append({'name':s['name'],'score':round(score,6),'matched_terms':sorted(shared),
                            'status':s['status'],'risk':s['risk'],'output':s['outputs']})
        results.sort(key=lambda x:(-x['score'],x['name']))
        return {'query':query,'method':'deterministic lexical TF-IDF cosine; not semantic inference',
                'abstained':not results,'results':results[:limit],
                'notice':'Scores measure textual relevance, not probability of correctness, safety, or authority. Nothing is executed.'}
