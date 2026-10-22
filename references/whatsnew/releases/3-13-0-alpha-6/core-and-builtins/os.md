# Python 3.13.0 alpha 6 / core and builtins / os

[gh-113964](https://github.com/python/cpython/issues/113964): Launching fresh threads and spawning processes via [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) are now blocked solely until every non-daemon thread has exited.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
