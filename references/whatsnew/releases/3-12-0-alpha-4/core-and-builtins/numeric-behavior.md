# Python 3.12.0 alpha 4 / core and builtins / numeric behavior

[gh-100188](https://github.com/python/cpython/issues/100188): Negative integer indices no longer route through the `BINARY_SUBSCR_LIST_INT` and `BINARY_SUBSCR_TUPLE_INT` instructions, since those paths invariably miss for any negative integer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
