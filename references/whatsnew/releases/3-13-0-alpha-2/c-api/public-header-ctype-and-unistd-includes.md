# Python 3.13.0 alpha 2 / c api / restore ctype h unistd h includes within python h while keeping them

[gh-112026](https://github.com/python/cpython/issues/112026): Restore the `<ctype.h>` and `<unistd.h>` includes within `Python.h`, while keeping them out of the limited C API for version 3.13 and later. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
