"""Explicit, local-only project installation with preflight, ownership and backups.

No shell, Git, cloud API, credential access or business-workflow execution.
Cooperating installers are serialized. This is not an OS security sandbox.
"""
from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
from typing import Any, Iterator
from uuid import uuid4
from .core import Catalog, CSSError, confined, digest, read_json, tree_files

PREFIX = {'claude':'.claude/skills','codex':'.agents/skills','generic':'exported-skills'}

def json_bytes(value: Any) -> bytes:
    return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()

def _allowed(rel: str, runtime: str) -> bool:
    return rel.startswith(PREFIX[runtime]+'/') or rel==f'.css/install-{runtime}.json'

def _current(root: Path, rel: str) -> bytes | None:
    p=confined(root,rel)
    if p.exists() and not p.is_file():raise CSSError(f'expected file, found directory: {rel}')
    return p.read_bytes() if p.is_file() else None

def _write(root: Path, rel: str, data: bytes) -> None:
    out=confined(root,rel);out.parent.mkdir(parents=True,exist_ok=True)
    # Recheck after directory creation. Atomic replacement stays on target filesystem.
    confined(root,rel)
    fd,tmp=tempfile.mkstemp(prefix='.css-stage-',dir=out.parent)
    try:
        with os.fdopen(fd,'wb') as f:
            f.write(data);f.flush();os.fsync(f.fileno())
        os.replace(tmp,out)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

@contextmanager
def lock(target: Path) -> Iterator[None]:
    p=confined(target,'.css/install.lock');p.parent.mkdir(parents=True,exist_ok=True)
    try:
        fd=os.open(p,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    except FileExistsError as exc:
        raise CSSError('another installer or stale lock exists; inspect .css/install.lock before recovery') from exc
    try:
        with os.fdopen(fd,'w') as f:f.write(str(os.getpid()))
        yield
    finally:
        p.unlink(missing_ok=True)

def install(catalog: Catalog, profile: str, target: Path, runtime: str='claude',
            apply: bool=False) -> dict[str,Any]:
    if runtime not in PREFIX:raise CSSError('unsupported runtime')
    target=target.absolute()
    if not target.is_dir() or target==Path(target.anchor):
        raise CSSError('target must be an existing, non-root project directory')
    confined(target,'.css/install.lock')
    validation=catalog.validate()
    if not validation['ok']:raise CSSError('source validation failed; run python -m css validate')
    selected=catalog.profile(profile)
    desired: dict[str,bytes]={}
    for name in selected:
        for rel,data in tree_files(catalog.root,f'skills/{name}').items():
            if rel=='SKILL.md' and runtime=='claude':
                text=data.decode('utf-8')
                text=text.replace('\n---\n','\ndisable-model-invocation: true\n---\n',1)
                data=text.encode()
            desired[f'{PREFIX[runtime]}/{name}/{rel}']=data
        if runtime=='codex':
            desired[f'{PREFIX[runtime]}/{name}/agents/openai.yaml']=b'policy:\n  allow_implicit_invocation: false\n'
    mrel=f'.css/install-{runtime}.json'
    old_manifest_bytes=_current(target,mrel)
    old_manifest=read_json(confined(target,mrel)) if old_manifest_bytes is not None else {'files':{}}
    if not isinstance(old_manifest,dict) or not isinstance(old_manifest.get('files'),dict):
        raise CSSError('invalid installation manifest')
    owned=old_manifest['files']
    for rel,h in owned.items():
        confined(target,rel)
        if not _allowed(rel,runtime) or not isinstance(h,str) or len(h)!=64:
            raise CSSError('unsafe installation manifest entry')
    plan=[]; conflicts=[]; before={}
    for rel,data in sorted(desired.items()):
        current=_current(target,rel);before[rel]=current
        if current is None:
            action='create'
        elif rel not in owned:
            action='conflict-unmanaged'
        elif digest(current)!=owned[rel]:
            action='conflict-local-edit'
        elif current==data:
            action='unchanged'
        else:
            action='update'
        if action.startswith('conflict'):conflicts.append(rel)
        plan.append({'path':rel,'action':action,'sha256':digest(data)})
    result={'runtime':runtime,'profile':profile,'skills':selected,'target':str(target),
            'applied':False,'plan':plan,'conflicts':conflicts,
            'notice':'Only selected instructions/resources are copied. No skills, Git commands or external workflows are executed.'}
    if not apply:return result
    if conflicts:raise CSSError('refusing to overwrite unmanaged or locally edited files: '+', '.join(conflicts[:5]))
    changed={item['path']:desired[item['path']] for item in plan if item['action']!='unchanged'}
    files={**owned,**{p:digest(b) for p,b in desired.items()}}
    new_manifest={'schema_version':'1.0','runtime':runtime,'package_version':catalog.raw['version'],
                  'files':files,'skills':sorted(set(old_manifest.get('skills',[]))|set(selected))}
    # Reinstalling identical content is a no-op. Do not erase previous managed profiles.
    manifest_bytes=json_bytes(new_manifest)
    if not changed and old_manifest_bytes==manifest_bytes:
        result['applied']=True;result['backup']=None;return result
    changed[mrel]=manifest_bytes;before[mrel]=old_manifest_bytes
    backup_id=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:12]
    backup_rel=f'.css/backups/{backup_id}'
    completed=[]
    with lock(target):
        for rel in changed:
            if _current(target,rel)!=before[rel]:
                raise CSSError(f'file changed during preflight: {rel}')
        journal={'schema_version':'1.0','runtime':runtime,'id':backup_id,'files':[]}
        for rel,data in changed.items():
            old=before[rel]
            journal['files'].append({'path':rel,'before_sha256':digest(old) if old is not None else None,'after_sha256':digest(data)})
            if old is not None:_write(target,f'{backup_rel}/files/{rel}',old)
        _write(target,f'{backup_rel}/journal.json',json_bytes(journal))
        try:
            for rel,data in changed.items():
                if _current(target,rel)!=before[rel]:raise CSSError(f'concurrent modification: {rel}')
                _write(target,rel,data);completed.append(rel)
        except Exception as exc:
            recovery=[]
            for rel in reversed(completed):
                try:
                    if before[rel] is None:confined(target,rel).unlink(missing_ok=True)
                    else:_write(target,rel,before[rel])
                except Exception as restore_exc:recovery.append(f'{rel}: {restore_exc}')
            raise CSSError(f'installation failed: {exc}; '+('rollback incomplete: '+str(recovery) if recovery else 'written files restored')+f'; backup {backup_id}') from exc
    result['applied']=True;result['backup']=backup_id
    return result

def restore(target: Path, backup_id: str, apply: bool=False) -> dict[str,Any]:
    import re
    if not re.fullmatch(r'\d{8}T\d{6}Z-[0-9a-f]{12}',backup_id):raise CSSError('invalid backup ID')
    target=target.absolute();base=f'.css/backups/{backup_id}'
    journal=read_json(confined(target,f'{base}/journal.json'))
    runtime=journal.get('runtime')
    if runtime not in PREFIX:raise CSSError('invalid backup runtime')
    changes={};present={};seen=set()
    for item in journal.get('files',[]):
        rel=item['path'];confined(target,rel)
        if rel in seen or not _allowed(rel,runtime):raise CSSError('unsafe or duplicate backup path')
        seen.add(rel)
        current=_current(target,rel)
        if current is None or digest(current)!=item['after_sha256']:
            raise CSSError(f'restore would overwrite edits or a later install: {rel}')
        present[rel]=current
        if item['before_sha256'] is None:changes[rel]=None
        else:
            prior=confined(target,f'{base}/files/{rel}').read_bytes()
            if digest(prior)!=item['before_sha256']:raise CSSError('backup integrity mismatch')
            changes[rel]=prior
    result={'backup':backup_id,'applied':False,'paths':list(changes),
            'notice':'Restore changes only this installation transaction. Empty directories may remain.'}
    if not apply:return result
    completed=[]
    with lock(target):
        try:
            for rel,prior in changes.items():
                if _current(target,rel)!=present[rel]:raise CSSError('concurrent target change')
                if prior is None:confined(target,rel).unlink()
                else:_write(target,rel,prior)
                completed.append(rel)
        except Exception as exc:
            failures=[]
            for rel in reversed(completed):
                try:_write(target,rel,present[rel])
                except Exception as err:failures.append(str(err))
            raise CSSError(f'restore failed: {exc}; rollback errors: {failures}') from exc
    result['applied']=True
    return result
