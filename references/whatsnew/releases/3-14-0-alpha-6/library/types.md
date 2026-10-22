# Python 3.14.0 alpha 6 / library / types

[gh-105499](https://github.com/python/cpython/issues/105499): [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) is now simply an alias of [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union). Writing either `int | str` or `Union[int, str]` yields instances of one and the same type. Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
