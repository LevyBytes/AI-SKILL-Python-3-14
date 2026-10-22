# Python 3.14.3 final / core and builtins / memory

[gh-143057](https://github.com/python/cpython/issues/143057): Skip locking inside [`PyTraceMalloc_Track()`](https://docs.python.org/3.14/c-api/memory.html#c.PyTraceMalloc_Track) and [`PyTraceMalloc_Untrack()`](https://docs.python.org/3.14/c-api/memory.html#c.PyTraceMalloc_Untrack) whenever [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) has not been turned on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
