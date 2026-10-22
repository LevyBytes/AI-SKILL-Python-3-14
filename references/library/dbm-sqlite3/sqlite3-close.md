# dbm.sqlite3 — **flag** (*str*) –

**flag** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) –
  - `'r'` (default): read-only access to a database that already exists.

  - `'w'`: read-and-write access to a database that already exists.

  - `'c'`: read-and-write access, building the database when it is not yet present.

  - `'n'`: always start a fresh, empty database with read-and-write access.

- **mode** – The file’s Unix access mode (octal `0o666` by default), applied solely at the moment a database must be created.

The database object you get back acts much like a mutable [mapping](https://docs.python.org/3.14/glossary.html#term-mapping), except that `keys()` yields a list and `setdefault()` demands two arguments. A “closing” context manager is also supported through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword.

The following method is also provided:

 sqlite3.close()

Close the SQLite database.

[Subject index](INDEX.md) · [Previous](dbm-sqlite3-open.md) · [Continue](../dbm-gnu/dbm-gnu-error-to-dbm-gnu-open.md) · [Owning module, declaration or section: dbm.sqlite3](dbm-sqlite3-open.md)
