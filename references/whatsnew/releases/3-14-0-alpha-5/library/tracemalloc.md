# Python 3.14.0 alpha 5 / library / tracemalloc

[gh-128679](https://github.com/python/cpython/issues/128679): [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc): Eliminate races triggered when one thread invokes [`tracemalloc.stop()`](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.stop) while other threads are still tracing allocations. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
