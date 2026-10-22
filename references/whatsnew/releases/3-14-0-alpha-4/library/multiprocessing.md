# Python 3.14.0 alpha 4 / library / multiprocessing

[gh-127586](https://github.com/python/cpython/issues/127586): [`multiprocessing.pool.Pool`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool) now correctly puts the parent thread's blocked signal handlers back when it spins up processes through either *spawn* or *forkserver*.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
