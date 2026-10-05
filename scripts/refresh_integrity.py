"""Review changed skill digests; explicit --apply updates registry after author review.

This does not confer authenticity, maturity, behavioral validation or approval.
"""
from pathlib import Path
import argparse
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from css.core import Catalog,CSSError,content_digest

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--apply',action='store_true');a=p.parse_args()
    c=Catalog(Path(__file__).resolve().parents[1]);validation=c.validate(integrity=False)
    if not validation['ok']:print(json.dumps(validation,indent=2));return 1
    changes=[]
    for s in c.skills:
        actual=content_digest(c.root,'skills/'+s['name'])
        if actual!=s['content_sha256']:
            changes.append({'name':s['name'],'before':s['content_sha256'],'after':actual});s['content_sha256']=actual
    print(json.dumps({'changes':changes,'applied':a.apply,'notice':'Review diffs before accepting new integrity hashes.'},indent=2))
    if a.apply:
        (c.root/'catalog/skill-registry.json').write_text(json.dumps(c.raw,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return 0
if __name__=='__main__':raise SystemExit(main())
