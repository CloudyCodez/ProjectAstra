"""Mirror only catalog-pinned release bytes; never access saves or keys."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
REPO='CloudyCodez/ProjectAstra'

def gh(*args):
    return subprocess.check_output(['gh',*args],text=True)

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('index',type=int)
    args=parser.parse_args()
    catalog=json.loads((ROOT/'distribution/asset-catalog.json').read_text())
    row=catalog['assets'][args.index]
    # Catalog edits are code-reviewed. A workflow input cannot select a URL.
    assert row['source_repository']=='CloudyCodez/eeeeeekkkkk'
    assert row['target_tag'] in ('PA-AV1','PA-DELTA-20261013')
    release=json.loads(gh('release','view',row['target_tag'],'--repo',REPO,'--json','assets,isDraft'))
    if not release['isDraft']:raise ValueError('Mirror requires a draft asset release')
    existing=next((a for a in release['assets'] if a['name']==row['name']),None)
    if existing:
        if existing['size']==row['bytes'] and existing.get('digest')=='sha256:'+row['sha256']:
            print('Already verified:',row['name']);return
        raise ValueError('Existing asset differs; refusing overwrite')
    with tempfile.TemporaryDirectory(prefix='astra-mirror-') as folder:
        gh('release','download',row['source_tag'],'--repo',row['source_repository'],
           '--pattern',row['name'],'--dir',folder)
        path=Path(folder)/row['name']
        if path.stat().st_size!=row['bytes'] or digest(path)!=row['sha256']:
            raise ValueError('Source content failed pinned integrity check')
        gh('release','upload',row['target_tag'],str(path),'--repo',REPO)
        print('Mirrored and verified:',row['name'])

if __name__=='__main__':main()
