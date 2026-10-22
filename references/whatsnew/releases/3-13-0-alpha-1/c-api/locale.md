# Python 3.13.0 alpha 1 / c api / locale

[gh-108765](https://github.com/python/cpython/issues/108765): The `<ctype.h>` standard header is no longer pulled in by `Python.h`. Include it directly when you need it. As an example, it supplies the locale-dependent `isalpha()` and `tolower()` functions. Locale independent equivalents such as `Py_ISALPHA()` and `Py_TOLOWER()` ship with Python. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
