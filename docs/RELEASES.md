# Release operations

This repository is the public distribution home. Binary payloads live in releases,
not Git. No signing secrets, saves, private logs or extracted client tables belong
in this repository.

## Initial asset migration

`distribution/asset-catalog.json` pins the source sizes and SHA-256 digests for
twelve baseline parts and one incremental part already published by CloudyCodez.

1. A maintainer creates draft `PA-AV1` and `PA-DELTA-20261013` asset releases.
2. Run **Actions → Mirror verified asset releases → Run workflow**.
3. Each job downloads one allowlisted source file, hashes it, uploads it to this
   repository, and skips an already matching upload on rerun. Conflicting assets
   are rejected, not overwritten. No local 9 GB re-upload is required.
4. `verify_releases.py` checks every target size and GitHub SHA-256 digest.
5. Upload the locally signed asset metadata, then publish the verified asset
   releases as non-latest releases. Publish the testing APK release last.

The workflow deliberately leaves publication to the maintainer so incomplete
assets cannot become the advertised installer. It requires only GitHub's scoped
workflow token; production signing keys never enter Actions.

## Future builds

Prepare and verify the APK/server payload locally, sign with the existing private
key, and publish a **new tag**. Never overwrite a published binary. Asset updates
must preserve pinned hashes, signed metadata and a known matching baseline.
Update the catalog for new asset sets and code-review it before mirroring.

Use `python scripts/verify_releases.py` with `GH_TOKEN` or an authenticated `gh`
session to audit the baseline and delta releases. Testing APKs ship SHA256SUMS
and build details separately. Do not mark an incomplete Big 100 build stable or
publish private diagnostics as release attachments.
