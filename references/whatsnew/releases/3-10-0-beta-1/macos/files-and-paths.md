# Python 3.10.0 beta 1 / macos / files and paths

[bpo-42119](https://bugs.python.org/issue?@action=redirect&bpo=42119): Corrected the macOS SDK path check performed while building Python. The search now matches only SDK contents — that is, just the files under `/System/Library`, `/System/IOSSupport`, and the parts of `/usr` apart from `/usr/local`. Earlier, everything beneath `/System` was assumed to belong to an SDK, which broke under the new 10.15+ file system layout where user file systems can appear mounted below `/System`. Locations under `/Library` were likewise mistaken for SDK paths.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
