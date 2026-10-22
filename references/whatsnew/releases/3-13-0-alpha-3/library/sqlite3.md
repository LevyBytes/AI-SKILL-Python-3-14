# Python 3.13.0 alpha 3 / library / sqlite3

[gh-108364](https://github.com/python/cpython/issues/108364): [`sqlite3.Connection.iterdump()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.iterdump) will now make certain that foreign key support is turned off ahead of dumping the database schema, should any foreign key violation exist. Erlend E. Aasland and Mariusz Felisiak supplied this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
