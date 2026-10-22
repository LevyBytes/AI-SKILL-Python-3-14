# Python 3.7.0 alpha 3 / core and builtins / locale

[bpo-28180](https://bugs.python.org/issue?@action=redirect&bpo=28180): To make behaviour line up better across the various `libc` implementations, a new internal helper `_Py_SetLocaleFromEnv(category)` has been introduced (Android, for instance, does not by default honour setting the locale from the environment).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
