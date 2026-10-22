# Python 3.14.5 release candidate 1 / core and builtins / sys

[gh-113956](https://github.com/python/cpython/issues/113956): Resolve a data race within [`sys.intern()`](https://docs.python.org/3.14/library/sys.html#sys.intern) on the free-threaded build that occurred while interning a string belonging to a different thread. When immortalizing the original is unsafe, an interned copy owned by the calling thread is substituted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
