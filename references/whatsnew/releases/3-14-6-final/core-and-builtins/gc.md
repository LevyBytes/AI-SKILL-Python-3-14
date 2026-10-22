# Python 3.14.6 final / core and builtins / gc

[gh-148613](https://github.com/python/cpython/issues/148613): Repair a data race within the free-threaded build occurring between [`gc.set_threshold()`](https://docs.python.org/3.14/library/gc.html#gc.set_threshold) and the scheduling of garbage collection during object allocation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
