# Python 3.11.0 alpha 7 / library / overview

When a BLOB conversion fails, leave [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError) intact instead of clobbering it with [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

  - Should a caller try to [`execute()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Cursor.execute) more than a single SQL statement, raise [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError) in place of [`Warning`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Warning).

  - Whenever an SQL query embeds null characters, raise [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
