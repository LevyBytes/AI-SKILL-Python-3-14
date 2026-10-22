# Python 3.12.0 alpha 6 / library / exceptions

[gh-101892](https://github.com/python/cpython/issues/101892): Callable iterators will no longer throw [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) where the callable object drains the iterator yet neglects either to return a sentinel value or to raise [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
