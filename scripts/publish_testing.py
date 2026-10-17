"""Create an APK testing release only after asset verification; no signing keys."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile
from verify_releases import main as verify_assets

REPO='CloudyCodez/ProjectAstra'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apk',type=Path,required=True)
    parser.add_argument('--details',type=Path,required=True)
    parser.add_argument('--notes',type=Path,required=True)
    parser.add_argument('--tag',required=True)
    parser.add_argument('--publish',action='store_true',help='Publish as latest after uploading; default draft')
    args=parser.parse_args()
    if not re.fullmatch(r'project-astra-r[0-9.]+-testing',args.tag):raise ValueError('Invalid testing tag')
    if args.apk.name!='project-astra-r99.9-testing.apk':
        # New revisions may use the same predictable naming convention.
        if not re.fullmatch(r'project-astra-r[0-9.]+-testing.apk',args.apk.name):raise ValueError('Invalid APK name')
    verify_assets()
    with zipfile.ZipFile(args.apk) as apk:
        config=json.loads(apk.read('assets/server-update-config.json'))
        if config['repository']!=REPO:raise ValueError('APK still points to another repository')
        if any(name.lower().endswith(('.p12','.keystore','.sqlite3')) for name in apk.namelist()):
            raise ValueError('Private data in APK')
    details=json.loads(args.details.read_text())
    if details['repository']!=REPO or details.get('saves_included') is not False:
        raise ValueError('Missing reviewed build details')
    digest=hashlib.sha256(args.apk.read_bytes()).hexdigest()
    details.update(apk=args.apk.name,apk_sha256=digest,apk_bytes=args.apk.stat().st_size,
        apk_signing_certificate_sha256='97c184a7a68c78d7c47ff2b73a396a378ae932fc17ce9c1de9b7fc02b70ecf73')
    with tempfile.TemporaryDirectory(prefix='astra-testing-release-') as folder:
        root=Path(folder)
        (root/'build-details.json').write_text(json.dumps(details,indent=2),encoding='utf8')
        notes=root/'INSTALL-AND-NOTES.md';notes.write_bytes(args.notes.read_bytes())
        checks=[f'{digest}  {args.apk.name}']
        for path in (root/'build-details.json',notes):
            checks.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.name)
        sums=root/'SHA256SUMS.txt';sums.write_text('\n'.join(checks)+'\n',encoding='utf8')
        subprocess.run(['gh','release','create',args.tag,str(args.apk),str(notes),
            str(root/'build-details.json'),str(sums),'--repo',REPO,'--draft',
            '--title','Project Astra '+config['display_revision']+' — Mobile & Emulator',
            '--notes-file',str(args.notes)],check=True)
        if args.publish:
            subprocess.run(['gh','release','edit',args.tag,'--repo',REPO,'--draft=false','--latest'],check=True)
    print('Testing release prepared:',args.tag,'SHA-256:',digest)

if __name__=='__main__':main()
