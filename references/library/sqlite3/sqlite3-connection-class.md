# sqlite3: `sqlite3.Connection`

### Connection objects

 *class *sqlite3.Connection

A `Connection` object stands for each open SQLite database, and you obtain one through `sqlite3.connect()`. Their chief role is producing `Cursor` objects, plus Transaction control.

See also

- How to use connection shortcut methods

- How to use the connection context manager

Changed in version 3.13: deleting a `Connection` object without having first called `close()` now emits a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

These are the attributes and methods an SQLite database connection carries:

[Subject index](INDEX.md) · [Previous](sqlite-database-configuration-flags.md) · [Continue](sqlite3-connection-cursor-to-sqlite3-connection-executescript.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
