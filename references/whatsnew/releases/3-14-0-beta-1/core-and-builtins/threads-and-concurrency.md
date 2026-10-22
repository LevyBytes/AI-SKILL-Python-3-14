# Python 3.14.0 beta 1 / core and builtins / threads and concurrency

[gh-132713](https://github.com/python/cpython/issues/132713): A `repr(list)` race condition is fixed by keeping a strong reference to the item across the `repr(item)` call. Victor Stinner wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
