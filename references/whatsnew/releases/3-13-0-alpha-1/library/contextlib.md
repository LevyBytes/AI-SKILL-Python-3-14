# Python 3.13.0 alpha 1 / library / contextlib

[gh-105726](https://github.com/python/cpython/issues/105726): Give [`contextlib.AbstractContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractContextManager) and [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/3.14/library/contextlib.html#contextlib.AbstractAsyncContextManager) a `__slots__` so that subclasses are free to rely on `__slots__` themselves.

[gh-110378](https://github.com/python/cpython/issues/110378): The [`contextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager) and [`asynccontextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.asynccontextmanager) context managers will now close an invalid underlying generator object whenever it yields more then one value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
