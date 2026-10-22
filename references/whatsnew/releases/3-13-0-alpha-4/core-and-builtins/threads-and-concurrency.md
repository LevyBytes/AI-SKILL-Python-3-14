# Python 3.13.0 alpha 4 / core and builtins / threads and concurrency

[gh-112529](https://github.com/python/cpython/issues/112529): The free-threaded build now ships its own thread-safe GC that relies on mimalloc to locate GC-tracked objects. Unlike the existing collector, it is non-generational.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
