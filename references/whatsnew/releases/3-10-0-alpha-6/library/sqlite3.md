# Python 3.10.0 alpha 6 / library / sqlite3

[bpo-43258](https://bugs.python.org/issue?@action=redirect&bpo=43258): Stop the unnecessary allocation of [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) aggregate function context whenever no rows satisfy an aggregate query. Erlend E. Aasland supplied the patch.

[bpo-43251](https://bugs.python.org/issue?@action=redirect&bpo=43251): Better [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) error reporting: a failed `sqlite3_column_name()` call now raises [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError). Erlend E. Aasland wrote the patch.

[bpo-40956](https://bugs.python.org/issue?@action=redirect&bpo=40956): A segfault in [`sqlite3.Connection.backup()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.backup) that struck when called with no argument is now fixed. PR 23838 had introduced this regression. Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
