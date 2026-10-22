# Python 3.14.5 release candidate 1 / core and builtins / types

[gh-148222](https://github.com/python/cpython/issues/148222): Repair vectorcall handling in [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias) for cases where the wrapped type lacks vectorcall support. Also seal off possible leaks affecting `types.GenericAlias` and [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) under a memory error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
