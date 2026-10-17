<div align="center">

# PROJECT ASTRA

### Your world. Your pace. Your local server.

[Download the testing build](https://github.com/CloudyCodez/ProjectAstra/releases/latest) · [Setup guide](docs/TESTING.md) · [Report a bug](https://github.com/CloudyCodez/ProjectAstra/issues/new/choose)

**Android mobile & emulators · Local profiles · Configurable progression**

</div>

---

Project Astra is an independent, in-development Epic Seven local-server testing
project. The Android hub starts the server on your own device and connects the
client through loopback. No separately hosted PC server is needed for this build.

## Start playing

1. Open the **latest testing release** and download the Project Astra APK.
2. Install it on your Android phone/tablet or Android emulator. Existing testers:
   update the installed app in place; **do not uninstall or clear its storage**.
3. Open **Project Astra**, choose a local profile and progression options, then
   tap **Start Server**. Allow the initial asset verification/download to finish.
4. Tap **Play** when the server is ready.

The APK is the installer. GitHub's automatically generated **Source code** ZIP
is not the game. You do not need to download asset parts manually.

## Built for testing

| Feature | What to expect |
| --- | --- |
| Android mobile | Local hub and server on supported Android devices |
| Android emulators | The same APK; compatibility depends on emulator Android/ABI support |
| Profiles & configuration | Vanilla-style progression or custom resource options |
| Assets | Verified downloads, reusable installed data, and compatible incremental updates |
| Restorations | Story, development, equipment, events and other systems under active testing |
| Offline guild simulation | Persistent NPC recruitment and daily attendance in the new testing build |

**This is a testing release—not a claim of 100% live-server parity.** Arena combat,
Guild War and some encounter mechanics remain incomplete or unverified. NPC
behavior is explicitly simulated, not online matchmaking or real players.

## Downloads, without the clutter

- **Testing release:** APK, installation notes, checksums and known issues.
- **Asset releases:** baseline parts and incremental asset updates used by the hub.
- **Repository:** documentation, issue templates and release automation—not private
  saves, account data, signing keys or raw analysis captures.

The first install downloads a large baseline. A compatible existing baseline is
reused for the smaller update. Fully verified cached parts are skipped on retry;
partial downloads resume when the host supports HTTP Range. Changing APKs does
not require deleting assets or profiles. See [testing and storage notes](docs/TESTING.md).

## THE BIG 100

Revision 100 is a milestone in progress, not a completion percentage. Priorities
include battle and boss accuracy, broader story/system restoration, offline Arena
opponents and guild activities. Release notes distinguish implemented features,
custom offline rules and remaining gaps.

## Credits

Created and maintained by **CloudyCodez**, with thanks to everyone testing and
reporting reproducible bugs.

Special thanks to **[REA — Reverse Engineer Anything](https://github.com/morluto/rea)**
for the tools and resources that enabled faster analysis, recovery and verification.
This credit does not imply endorsement or affiliation.

Epic Seven and its characters, artwork and other original content belong to their
respective rights holders. Project Astra is an independent fan/testing project and
is not affiliated with or endorsed by the original game's developers or publishers.
