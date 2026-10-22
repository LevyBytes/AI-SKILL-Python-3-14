# Python 3.12.0 alpha 6 / library / bdb

[gh-101517](https://github.com/python/cpython/issues/101517): Fixed a defect where [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) looks the source line up via [`linecache`](https://docs.python.org/3.14/library/linecache.html#module-linecache) with `lineno=None`, making it fail with an unhandled exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
