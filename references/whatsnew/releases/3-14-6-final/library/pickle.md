# Python 3.14.6 final / library / pickle

[gh-146452](https://github.com/python/cpython/issues/146452): Repair a segfault within [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) while pickling a dictionary that another thread mutates concurrently in the free-threaded build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
