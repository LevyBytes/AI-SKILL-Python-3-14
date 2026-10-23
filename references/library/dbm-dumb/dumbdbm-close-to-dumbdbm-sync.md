# dbm.dumb - **flag** (*str*) –

**flag** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) –
  - `'r'`: Open existing database for reading only.

  - `'w'`: read-and-write access to a database that already exists.

  - `'c'` (default): read-and-write access, building the database when it is not yet present.

  - `'n'`: always start a fresh, empty database with read-and-write access.

- **mode** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The file’s Unix access mode (octal `0o666` by default), applied solely at the moment a database must be created.

Warning

Loading a database that contains a sufficiently large or complex entry can crash the Python interpreter, owing to stack depth limits in Python’s AST compiler.

Changed in version 3.5: when *flag* is `'n'`, `open()` invariably builds a brand-new database.

Changed in version 3.8: with *flag* set to `'r'`, the database opens read-only. With *flag* set to `'r'` or `'w'`, a missing database is not created.

Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

The database object handed back acts much like a mutable [mapping](https://docs.python.org/3.14/glossary.html#term-mapping), except that both `keys()` and `items()` yield lists and `setdefault()` demands two arguments. A “closing” context manager is also supported through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword.

The following methods are also provided:

 dumbdbm.close()

Close the database.

 dumbdbm.sync()

Flush the directory and data files held on disk into sync. The [`shelve.Shelf.sync()`](https://docs.python.org/3.14/library/shelve.html#shelve.Shelf.sync) method invokes this one.

[Subject index](INDEX.md) · [Previous](dbm-dumb-error-to-filename-dir.md) · [Continue](../debug/debugging-and-profiling.md) · [Owning module, declaration or section: dbm.dumb](dbm-dumb-error-to-filename-dir.md)
