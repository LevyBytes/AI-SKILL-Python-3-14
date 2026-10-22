# Python 3.11.0 alpha 3 / library / sqlite3

[bpo-45754](https://bugs.python.org/issue?@action=redirect&bpo=45754): Correct a regression present in Python 3.11a1 and 3.11a2 in which [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) mistakenly applied `SQLITE_LIMIT_LENGTH` when validating SQL statement lengths. From now on `SQLITE_LIMIT_SQL_LENGTH` is what gets used. Erlend E. Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
