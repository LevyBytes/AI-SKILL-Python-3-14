# Python 3.14.3 final / library / atexit

[gh-142881](https://github.com/python/cpython/issues/142881): Concurrent and reentrant invocation of [`atexit.unregister()`](https://docs.python.org/3.14/library/atexit.html#atexit.unregister) is now fixed.

[gh-112127](https://github.com/python/cpython/issues/112127): A possible use-after-free in [`atexit.unregister()`](https://docs.python.org/3.14/library/atexit.html#atexit.unregister), occurring when the callback is unregistered during comparison, is now fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
