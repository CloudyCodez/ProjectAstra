# Testing setup

## Supported targets

Use the Android APK on an Android phone/tablet **or an Android emulator** with a
compatible ABI. Emulator support is not Windows-native support; install the APK
inside the emulator. This is not an iOS build. Minimum Android/API and packaged
ABIs are listed in each release's build details; device compatibility still needs
testing. No root or separate PC server is required for the local hub.

## Fresh install

1. Download the APK from the latest testing release. Verify its SHA-256 against
   `SHA256SUMS.txt` if desired. Only trust releases in this repository.
2. Permit installation from your browser/file manager when Android asks.
3. Open Project Astra. Select a profile, progression mode and optional settings.
4. Use Wi-Fi for the first asset download. Leave ample free storage for downloaded
   archives, installed data, update staging and rollback files. The baseline archive
   alone is approximately **9.38 GB**; this is not the total storage requirement.
5. Tap **Start Server**, wait for the ready status, then **Play**.

Internet is required to fetch releases/assets. Gameplay uses the local server;
some optional update checks may still try the network.

## Existing testers

Install the newer APK **over** the old one. Keep the same package/signature and do
not uninstall, clear app data or manually remove asset directories. Switching to
this repository requires the new distribution APK; older APKs still point to the
previous release feed. Keep a backup before trying experimental builds.

The hub verifies installed data and reuses a matching baseline. The October 13
incremental package is about **106.8 MB**, not another complete baseline. Invalid
or missing baseline data may still require the baseline download.

If interrupted, reopen the hub and start again. Verified cached parts are skipped;
partial downloads are resumed where the host supports it. Verification and local
patching can take time and are **not** full downloads. Internal/external storage
promotion uses the cross-filesystem-safe updater.

## Troubleshooting

| Symptom | First check |
| --- | --- |
| Play is disabled | Wait for the server-ready status; inspect the saved error |
| Assets appear to download again | Distinguish verification/local merge from network transfer; do not clear cache |
| Startup storage error | Free space without deleting the profile or active asset files |
| Android refuses the update | Check package/signature compatibility; do not uninstall as a first step |
| Hub controls/text clipped | Use the newest distribution APK and report resolution/font scale |
| A restored mode stalls | Copy diagnostics and report the exact stage/action and installed revision |

## Useful bug reports

Include APK filename, installed server revision, phone/emulator model, Android
version, profile mode, exact stage/menu, reproduction steps and expected result.
Attach the hub's **Copy diagnostics** output after reviewing it for private data.
Never post account credentials, tokens, signing keys or a complete private save.

## Known limits

Not all live-server systems, boss mechanics, waves, RNG or schedules have been
verified. Offline event availability and NPC guild activity are custom rules.
Arena combat and Guild War are not ready in this testing release. See each
release's notes rather than assuming revision 100 means complete parity.
