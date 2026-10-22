# Python 3.14.1 final / core and builtins / stdtypes

[gh-132657](https://github.com/python/cpython/issues/132657): Raise the performance of [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) by stripping out locks under the free-threading build.

[gh-140551](https://github.com/python/cpython/issues/140551): Resolved a crash within [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) whenever [`dict.clear()`](https://docs.python.org/3.14/library/stdtypes.html#dict.clear) gets invoked during the lookup stage. Mikhail Efimov along with Inada Naoki supplied the patch.

[gh-140939](https://github.com/python/cpython/issues/140939): Resolve a memory leak occurring when [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) gets formated through the `%*b` format using a large width that ends in a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
