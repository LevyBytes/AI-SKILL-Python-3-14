# Python 3.12.0 alpha 2 / core and builtins / imports and modules

[gh-90716](https://github.com/python/cpython/issues/90716): Introduce the _pylong.py module. It bundles asymptotically quicker algorithms suited to operations on integers carrying many digits. longobject.c draws on it to accelerate a handful of operations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
