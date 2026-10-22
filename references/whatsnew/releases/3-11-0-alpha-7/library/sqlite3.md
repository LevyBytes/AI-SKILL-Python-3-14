# Python 3.11.0 alpha 7 / library / sqlite3

[bpo-44859](https://bugs.python.org/issue?@action=redirect&bpo=44859): Exceptions raised by [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) are now more precise and better aligned with [**PEP 249**](https://peps.python.org/pep-0249/).

  - For `SQLITE_MISUSE` errors, raise [`InterfaceError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.InterfaceError) rather than [`ProgrammingError`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.ProgrammingError).

[bpo-41930](https://bugs.python.org/issue?@action=redirect&bpo=41930): [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) gains [`serialize()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.serialize) and [`deserialize()`](https://docs.python.org/3.14/library/sqlite3.html#sqlite3.Connection.deserialize) support. Erlend E. Aasland contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
