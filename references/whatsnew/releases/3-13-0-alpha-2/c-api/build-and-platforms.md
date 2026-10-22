# Python 3.13.0 alpha 2 / c api / build and platforms

[gh-108765](https://github.com/python/cpython/issues/108765): Under Windows, the `<stddef.h>` standard header is no longer pulled in by `Python.h`. Code that relies on it must now bring it in directly. Victor Stinner contributed the fix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
