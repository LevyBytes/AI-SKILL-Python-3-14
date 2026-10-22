# Python 3.14.0 beta 1 / library / concurrent futures

[gh-132063](https://github.com/python/cpython/issues/132063): Keep exceptions that test as falsey (that is, when their `__bool__` method yields `False` or their `__len__` method yields 0) from being silently dropped by [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) and [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
