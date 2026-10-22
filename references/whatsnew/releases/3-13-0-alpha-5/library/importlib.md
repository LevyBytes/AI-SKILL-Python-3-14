# Python 3.13.0 alpha 5 / library / importlib

[gh-114763](https://github.com/python/cpython/issues/114763): Guard modules brought in through [`importlib.util.LazyLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.util.LazyLoader) against the race that occurs when several threads reach for attributes while loading is still in progress.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
