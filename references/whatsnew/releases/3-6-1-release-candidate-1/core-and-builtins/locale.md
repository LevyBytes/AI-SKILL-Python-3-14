# Python 3.6.1 release candidate 1 / core and builtins / locale

[bpo-26919](https://bugs.python.org/issue?@action=redirect&bpo=26919): Under Android, operating system data now always gets encoded/decoded to/from UTF-8 in place of the locale encoding, sidestepping inconsistencies with os.fsencode() and os.fsdecode(), which already rely on UTF-8.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
