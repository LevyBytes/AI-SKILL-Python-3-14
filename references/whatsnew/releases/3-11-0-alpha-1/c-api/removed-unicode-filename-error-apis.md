# Python 3.11.0 alpha 1 / c api / removed unicode filename error apis

[bpo-44094](https://bugs.python.org/issue?@action=redirect&bpo=44094): Drop `PyErr_SetFromErrnoWithUnicodeFilename()`, `PyErr_SetFromWindowsErrWithUnicodeFilename()`, and `PyErr_SetExcFromWindowsErrWithUnicodeFilename()`. None are documented and all have carried a deprecation since Python 3.3.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
