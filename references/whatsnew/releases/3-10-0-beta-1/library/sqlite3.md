# Python 3.10.0 beta 1 / library / sqlite3

[bpo-43752](https://bugs.python.org/issue?@action=redirect&bpo=43752): Fix the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) regression affecting zero-sized blobs with converters, where `b""` came back rather than `None`. PR 24723 had introduced that regression. Erlend E. Aasland wrote the patch.

[bpo-43296](https://bugs.python.org/issue?@action=redirect&bpo=43296): Better error reporting in [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3): when `sqlite3_value_blob()` fails and sets `SQLITE_NOMEM`, a [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) is now raised. Erlend E. Aasland supplied the patch.

[bpo-43265](https://bugs.python.org/issue?@action=redirect&bpo=43265): Better error reporting for [`sqlite3.Connection.backup()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.backup). When a target database name does not exist, the reported message reads `unknown database <database name>` rather than the former `SQL logic error`. Erlend E. Aasland wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
