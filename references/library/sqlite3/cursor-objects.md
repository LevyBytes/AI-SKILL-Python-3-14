# sqlite3: Cursor inserted-row identity and result metadata

lastrowid

A read-only attribute exposing the row id of the most recently inserted row. Updates happen solely after a successful `INSERT` or `REPLACE` run through the `execute()` method. With any other statements, following `executemany()` or `executescript()`, or when an insert fails, `lastrowid` keeps its prior value. At the start, `lastrowid` holds `None`.

Note

Rows added to `WITHOUT ROWID` tables go unrecorded.

Changed in version 3.6: Added support for the `REPLACE` statement.

 rowcount

A read-only attribute exposing how many rows were altered by `INSERT`, `UPDATE`, `DELETE`, and `REPLACE` statements; it reads `-1` for everything else, CTE queries included. Only the `execute()` and `executemany()` methods refresh it, once the statement has finished running. As a result, you must fetch any rows produced before `rowcount` reflects them.

 row_factory

Determines how a row read from this `Cursor` is presented. With `None`, the row appears as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple). You may assign the bundled `sqlite3.Row`, or a [callable](https://docs.python.org/3.14/glossary.html#term-callable) taking two arguments, namely a `Cursor` object plus the `tuple` of row values, that returns a custom object standing in for an SQLite row.

Its default mirrors whatever `Connection.row_factory` held at the moment the `Cursor` was built. Setting this attribute leaves the parent connection's `Connection.row_factory` untouched.

See How to create and use row factories for more details.

Changed in version 3.14.6: The `row_factory` attribute can no longer be deleted.

[Subject index](INDEX.md) · [Previous](sqlite3-cursor-executescript-to-sqlite3-cursor-setoutputsize.md) · [Continue](sqlite3-row-class.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md) · [Owning module, declaration or section: sqlite3.Cursor](sqlite3-cursor-class.md) · [Owning module, declaration or section: Cursor objects](sqlite3-cursor-class.md)
