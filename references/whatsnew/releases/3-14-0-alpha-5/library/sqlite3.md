# Python 3.14.0 alpha 5 / library / sqlite3

[gh-129603](https://github.com/python/cpython/issues/129603): Resolve crashes where [`sqlite3.Row`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Row) instances could segfault whenever their inherited [`description`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.description) had been assigned `None`. Erlend Aasland wrote the patch.

[gh-129346](https://github.com/python/cpython/issues/129346): Within [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3), gracefully handle out-of-memory situations while constructing user-defined SQL functions.

[gh-129928](https://github.com/python/cpython/issues/129928): Creating a user-defined SQL function with an invalid number of parameters now raises [`sqlite3.ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError). Erlend Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
