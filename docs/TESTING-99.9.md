# Project Astra 99.9 — testing distribution

The new home for Project Astra testing: one installer release and separate,
automatically fetched asset releases.

## Install

Download **project-astra-r99.9-testing.apk**. Install it on Android mobile or a
compatible Android emulator, open Project Astra, choose a profile and tap
**Start Server**. Wait for ready, then **Play**. The APK bundles the local server;
there is no PC server to configure.

**Android 8.0+ · ARM64 · package `com.cloud.e7offline`**. x86/x64 emulators require
ARM64 translation. Device/emulator compatibility is not universally verified.

Existing testers: install over the old APK. **Do not uninstall or clear storage.**
The established signing certificate is retained. Old APKs still use the old
repository; this APK changes the asset/update home to ProjectAstra.

## In this build

- Native Project Astra hub with scrollable server controls, wrapped settings
  choices, and system/keyboard inset handling from the phone-layout hotfix.
- Latest locally verified story, equipment, Forge, event and progression fixes.
- Persistent offline guild NPC recruitment from committed clears/donations,
  activity-based NPC growth, daily check-in and attendance-tier rewards.
- Explicit offline NPC attendance; no fabricated remote players or multiplayer.
- Verified/resumable baseline fetching, matching-baseline incremental updates,
  and cross-filesystem-safe Android asset promotion.
- Asset and optional signed server-update discovery now use this repository.

## Downloads and storage

The hub downloads assets automatically. The fresh baseline archive is roughly
9.38 GB, split into twelve verified parts. The matching October 13 delta is
approximately 106.8 MB. These are separate from the APK. Verification and local
merging are not repeated full downloads. Keep ample room for installation,
download cache, staging and rollback; the archive size is not the total needed.

Do not extract parts manually or download GitHub's Source code ZIP as an installer.

## Validation and known limits

The packaged gameplay candidate passed **169 tests, with 2 workspace-only tests
skipped**. Temporary-save upgrade checks passed. All **19** retained native Lua
harnesses passed with rendering/unrelated services stubbed. Feed migration and
downloader checks passed **72 tests**. These are local verification results,
not a full device playthrough or proof of live-server parity.

**Arena combat and Guild War are not ready.** Some boss mechanics, encounter
waves and other systems remain incomplete/unverified. This release has not had
a fresh end-to-end device test. The hub's static control-room heading may still
show 99.8; installed server display/build details identify this 99.9 testing APK.
THE BIG 100 remains in development—not a completion percentage.

## Feedback and credits

Report the exact APK/server revision, stage/action, device/emulator and reproduction
steps. Review **Copy diagnostics** before sharing; do not post private saves or keys.

Thanks to CloudyCodez and the testers. Special credit to
**[REA — Reverse Engineer Anything](https://github.com/morluto/rea)** for tools and
resources enabling faster analysis and verification. Independent fan/testing
project; no affiliation with the original game's creators or with REA is implied.
