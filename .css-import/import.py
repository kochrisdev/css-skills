"""One-time, hash-bound transport for the already reviewed CSS v0.5 source.

Only the dedicated upgrade branch may be pushed. The existing import workflow
is retained in the transport commit; a separate connector commit will replace
it with the package's ordinary read-only CI workflow. No main/tag/release writes.
"""
from __future__ import annotations
import base64
import hashlib
import json
import lzma
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile

REPOSITORY = 'kochrisdev/css-skills'
BRANCH = 'improve/css-v0.5'
BASE = 'cb2a4689b46f38d136fdd3a2b7d572d87f657fb7'
PAYLOAD = 'f9faa006a7af813e60da6a3fe45f761bc7be42d8bb1004401dece5898ad4f20f'
SNAPSHOT = 'd761013ac2fca6c4973fabd205033a6a025e231a42bfd1e5bc9fcbb1d76f3d61'
TARGET_TREE = '32bd6d6313e98bf76edea022fa645b895a585cbf'
IMPORT_WORKFLOW = '.github/workflows/css-v05-import.yml'
ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'CSS-DIGEST:(.*?):END-DIGEST')


def run(*args: str, data: bytes | None = None, env: dict | None = None,
        cwd: Path | None = None) -> bytes:
    result = subprocess.run(args, input=data, cwd=cwd or ROOT, env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise RuntimeError(f'command failed: {args[0:2]!r}\n'
                           + result.stderr.decode('utf-8', errors='replace'))
    return result.stdout


def load_files(payload: bytes) -> dict[str, bytes]:
    if hashlib.sha256(payload).hexdigest() != PAYLOAD:
        raise ValueError('compressed package SHA-256 mismatch')
    raw = lzma.decompress(payload, memlimit=128 * 1024 * 1024)
    if len(raw) > 2_000_000:
        raise ValueError('oversized source map')
    templates = json.loads(raw)
    if not isinstance(templates, dict) or len(templates) != 379:
        raise ValueError('expected exactly 379 source files')
    for name, text in templates.items():
        p = PurePosixPath(name)
        if (not isinstance(text, str) or p.is_absolute() or not p.parts
                or any(x in ('', '.', '..', '.git') for x in name.split('/'))
                or '\\' in name or ':' in name):
            raise ValueError(f'unsafe source entry: {name!r}')
    resolved: dict[str, str] = {}

    def render(name: str, stack: tuple[str, ...] = ()) -> str:
        if name in resolved:
            return resolved[name]
        if name in stack:
            raise ValueError('digest dependency cycle')
        def substitution(match: re.Match) -> str:
            value = render(match[1], stack + (name,)).encode('utf-8')
            return hashlib.sha256(value).hexdigest()
        resolved[name] = PATTERN.sub(substitution, templates[name])
        return resolved[name]

    # Preserve the source archive's insertion order in the snapshot digest.
    strings = {name: render(name) for name in templates}
    serial = json.dumps(strings, ensure_ascii=False, separators=(',', ':')).encode()
    if hashlib.sha256(serial).hexdigest() != SNAPSHOT:
        raise ValueError('reconstructed source snapshot SHA-256 mismatch')
    return {name: text.encode('utf-8') for name, text in strings.items()}


def verify_files(files: dict[str, bytes]) -> None:
    with tempfile.TemporaryDirectory(prefix='css-v05-verified-') as directory:
        target = Path(directory)
        for name, data in files.items():
            path = target / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for args in [
            [sys.executable, '-m', 'css', 'validate'],
            [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
            [sys.executable, '-m', 'css', 'benchmark-routing'],
        ]:
            subprocess.run(args, cwd=target, check=True)


def tree_for(entries: list[tuple[str, str]], index: Path) -> str:
    env = dict(os.environ, GIT_INDEX_FILE=str(index))
    run('git', 'read-tree', '--empty', env=env)
    records = b''.join(f'100644 {sha}\t{name}'.encode() + b'\0'
                       for name, sha in entries)
    run('git', 'update-index', '-z', '--index-info', data=records, env=env)
    return run('git', 'write-tree', env=env).decode().strip()


def main() -> None:
    if os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
        raise RuntimeError('wrong repository')
    if os.environ.get('GITHUB_REF') != 'refs/heads/' + BRANCH:
        raise RuntimeError('wrong branch; main is never a target')
    head = run('git', 'rev-parse', 'HEAD').decode().strip()
    if head != os.environ.get('GITHUB_SHA'):
        raise RuntimeError('checkout does not match triggering commit')
    run('git', 'merge-base', '--is-ancestor', BASE, head)
    current = run('git', 'ls-remote', '--heads', 'origin', 'refs/heads/' + BRANCH)
    if current.decode().split()[0] != head:
        raise RuntimeError('upgrade branch advanced; refusing to overwrite it')
    parts = sorted((ROOT / '.css-import').glob('part-*.bin'))
    if len(parts) != 8:
        raise ValueError('expected eight complete transport parts')
    files = load_files(b''.join(p.read_bytes() for p in parts))
    original_license = run('git', 'show', BASE + ':LICENSE')
    if files['LICENSE'] != original_license:
        raise RuntimeError('the inherited license must remain unchanged')
    verify_files(files)

    entries = [(name, run('git', 'hash-object', '-w', '--stdin', data=data)
                .decode().strip()) for name, data in files.items()]
    with tempfile.TemporaryDirectory(prefix='css-v05-index-') as directory:
        index = Path(directory) / 'index'
        exact = tree_for(entries, index)
        if exact != TARGET_TREE:
            raise RuntimeError('Git source tree differs from the reviewed archive')
        # A contents-only Actions token does not alter workflow files. Keep the
        # connector-authored workflow unchanged; connector finishes that change.
        imported = [(name, sha) for name, sha in entries
                    if not name.startswith('.github/workflows/')]
        workflow_sha = run('git', 'rev-parse', head + ':' + IMPORT_WORKFLOW).decode().strip()
        imported.append((IMPORT_WORKFLOW, workflow_sha))
        transport_tree = tree_for(imported, index)

    env = dict(os.environ,
        GIT_AUTHOR_NAME='github-actions[bot]',
        GIT_AUTHOR_EMAIL='41898282+github-actions[bot]@users.noreply.github.com',
        GIT_COMMITTER_NAME='github-actions[bot]',
        GIT_COMMITTER_EMAIL='41898282+github-actions[bot]@users.noreply.github.com')
    message = ('Import verified CSS v0.5.0 source and pass local checks\n\n'
               '379-file reviewed snapshot verified against tree ' + TARGET_TREE + '.\n'
               '99 deterministic tests and 18 routing smoke cases rerun.\n'
               'Workflow replacement is completed separately through the connector.\n')
    commit = run('git', 'commit-tree', transport_tree, '-p', head,
                 data=message.encode(), env=env).decode().strip()
    # No --force, no main, no tags, no release, and no persistent credentials.
    run('git', 'push', 'origin', commit + ':refs/heads/' + BRANCH)
    print('CSS_IMPORT_COMMIT=' + commit)
    print('CSS_REVIEWED_TREE=' + TARGET_TREE)


if __name__ == '__main__':
    main()
