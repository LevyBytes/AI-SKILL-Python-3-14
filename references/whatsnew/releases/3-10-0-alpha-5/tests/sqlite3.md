# Python 3.10.0 alpha 5 / tests / sqlite3

[bpo-40823](https://bugs.python.org/issue?@action=redirect&bpo=40823): Swap in `unittest.TestLoader().loadTestsFromTestCase()` where the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) tests had used `unittest.makeSuite()`. Erlend E. Aasland contributed the patch.

[bpo-40810](https://bugs.python.org/issue?@action=redirect&bpo=40810): Within [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3), repair `CheckTraceCallbackContent` for SQLite versions before 3.7.15.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
