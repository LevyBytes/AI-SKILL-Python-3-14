# Python 3.14.1 final / security / sqlite3

[gh-139283](https://github.com/python/cpython/issues/139283): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3): handle the maximum row count to fetch correctly in [`Cursor.fetchmany`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.fetchmany) and turn down negative values for [`Cursor.arraysize`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.arraysize). Bénédikt Tran authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
