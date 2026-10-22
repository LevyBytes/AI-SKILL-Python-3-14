# Python 3.12.0 alpha 7 / core and builtins / memory and lifetimes

[gh-102281](https://github.com/python/cpython/issues/102281): Close a possible nullptr dereference along with a use of uninitialized memory inside fileutils. Max Bachmann supplied the patch.

[gh-102300](https://github.com/python/cpython/issues/102300): Within float specializations of BINARY_OP, recycle operands whose refcount sits at 1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
