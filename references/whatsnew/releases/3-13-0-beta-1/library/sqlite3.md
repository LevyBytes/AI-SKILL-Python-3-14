# Python 3.13.0 beta 1 / library / sqlite3

[gh-118221](https://github.com/python/cpython/issues/118221): A defect where [`sqlite3.Connection.iterdump()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.iterdump) might break when a custom [`row factory`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.row_factory) had been set is now corrected. Erlend Aasland supplied the patch.

[gh-118406](https://github.com/python/cpython/issues/118406): Supply a signature for [`sqlite3.Connection`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection) objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
