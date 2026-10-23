# dbm.ndbm - **flag** (*str*) –

**flag** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) –
  - `'r'` (default): read-only access to a database that already exists.

  - `'w'`: read-and-write access to a database that already exists.

  - `'c'`: read-and-write access, building the database when it is not yet present.

  - `'n'`: always start a fresh, empty database with read-and-write access.

- **mode** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The file’s Unix access mode (octal `0o666` by default), applied solely at the moment a database must be created.

Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for filename.

`ndbm` objects act much like mutable [mappings](https://docs.python.org/3.14/glossary.html#term-mapping), although the `items()`, `values()`, `pop()`, `popitem()`, and `update()` methods are absent, `keys()` yields a list, and `setdefault()` needs two arguments. A “closing” context manager is also offered through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword.

Changed in version 3.2: Added the `get()` and `setdefault()` methods.

Changed in version 3.13: Added the `clear()` method.

The following method is also provided:

 ndbm.close()

Close the NDBM database.

[Subject index](INDEX.md) · [Previous](dbm-ndbm-error-to-dbm-ndbm-open.md) · [Continue](../dbm-dumb/dbm-dumb-error-to-filename-dir.md) · [Owning module, declaration or section: dbm.ndbm](dbm-ndbm-error-to-dbm-ndbm-open.md)
