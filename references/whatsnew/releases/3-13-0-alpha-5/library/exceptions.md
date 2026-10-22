# Python 3.13.0 alpha 5 / library / exceptions

[gh-114709](https://github.com/python/cpython/issues/114709): Passing an empty iterable to `posixpath.commonpath()` now produces a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); the prior behavior raised [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

When `None` is supplied, `posixpath.commonpath()` now produces a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) instead of the [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) that was raised before.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
