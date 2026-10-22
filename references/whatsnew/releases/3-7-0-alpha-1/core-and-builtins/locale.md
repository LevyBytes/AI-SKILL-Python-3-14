# Python 3.7.0 alpha 1 / core and builtins / locale

[bpo-28180](https://bugs.python.org/issue?@action=redirect&bpo=28180): [**PEP 538**](https://peps.python.org/pep-0538/) (legacy C locale coercion) is now implemented. The upshot: whenever a fitting coercion target locale exists, both the core interpreter and locale-aware C extensions will treat UTF-8, not ASCII, as the default text encoding.

[bpo-26920](https://bugs.python.org/issue?@action=redirect&bpo=26920): Repair the failure to obtain the locale's charset while the interpreter starts up, on the platforms that lack langinfo.

[bpo-26919](https://bugs.python.org/issue?@action=redirect&bpo=26919): On Android, operating system data is henceforth always encoded and decoded via UTF-8 rather than the locale encoding, sidestepping clashes with os.fsencode() and os.fsdecode(), which already rely on UTF-8.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
