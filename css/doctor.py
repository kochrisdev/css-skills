"""Read-only local diagnostics; does not initialize, clone, delete or modify Git."""
from pathlib import Path
import shutil
import subprocess
import sys

def diagnose(project: Path) -> dict:
    project=project.absolute()
    result={'project':str(project),'python':sys.version.split()[0],'exists':project.is_dir(),
            'git_available':bool(shutil.which('git')),'git_repository':False,'modified_files':None}
    if not project.is_dir():
        result['next_step']='Choose an existing project directory.';return result
    if not result['git_available']:
        result['next_step']='Install Git or select a shell where Git is available.';return result
    def run(*args):
        return subprocess.run(['git','-C',str(project),*args],capture_output=True,text=True,timeout=10)
    try:
        top=run('rev-parse','--show-toplevel')
        if top.returncode:
            result['next_step']='This folder is not inside a Git working tree. Locate your existing clone; do not delete folders or run git init blindly.'
            return result
        result['git_repository']=True;result['repository_root']=top.stdout.strip()
        branch=run('branch','--show-current')
        result['branch']=branch.stdout.strip() or '(detached HEAD)'
        status=run('status','--porcelain')
        result['modified_files']=len(status.stdout.splitlines()) if status.returncode==0 else None
        result['is_repository_root']=Path(top.stdout.strip()).resolve()==project.resolve()
        result['installed_claude_skills']=len(list((project/'.claude/skills').glob('*/SKILL.md')))
        result['next_step']='Preserve local changes. Review the upgrade patch with git apply --check before applying it.'
    except (OSError,subprocess.TimeoutExpired) as exc:
        result['error']=str(exc)
    return result
