"""Check GitHub sizes/digests for all catalog artifacts; fail closed."""
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
def main():
    rows=json.loads((ROOT/'distribution/asset-catalog.json').read_text())['assets']
    for tag in sorted({r['target_tag'] for r in rows}):
        release=json.loads(subprocess.check_output(['gh','release','view',tag,'--repo',
            'CloudyCodez/ProjectAstra','--json','assets'],text=True))
        assets={r['name']:r for r in release['assets']}
        for row in rows:
            if row['target_tag']!=tag:continue
            actual=assets.get(row['name'],{})
            if actual.get('size')!=row['bytes'] or actual.get('digest')!='sha256:'+row['sha256']:
                raise ValueError('Unverified release artifact: '+tag+'/'+row['name'])
        print('Verified:',tag)

if __name__=='__main__':main()
