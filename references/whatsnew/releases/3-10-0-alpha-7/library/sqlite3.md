# Python 3.10.0 alpha 7 / library / sqlite3

[bpo-43369](https://bugs.python.org/issue?@action=redirect&bpo=43369): Strengthen [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) error handling: a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) is now raised whenever `sqlite3_column_text()` and `sqlite3_column_blob()` set `SQLITE_NOMEM`. Erlend E. Aasland wrote the patch.

[bpo-43368](https://bugs.python.org/issue?@action=redirect&bpo=43368): Correct a [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) regression from PR 24562 in which an empty bytestring came back as `None` rather than `b''`. Mariusz Felisiak wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
