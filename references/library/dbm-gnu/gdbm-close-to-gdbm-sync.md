# dbm.gnu — **flag** (*str*) –

**flag** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) –
  - `'r'` (default): read-only access to a database that already exists.

  - `'w'`: read-and-write access to a database that already exists.

  - `'c'`: read-and-write access, building the database when it is not yet present.

  - `'n'`: always start a fresh, empty database with read-and-write access.

You may tack on the extra characters below to govern the way the database is opened:

  - `'f'`: launch the database in fast mode, where writes to it are left unsynchronized.

  - `'s'`: synchronized mode, in which each database change is flushed to the file at once.

  - `'u'`: Do not lock database.

Which flags are valid varies across GDBM versions. Consult the `open_flags` member to see the flag characters that are supported.

- **mode** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The file’s Unix access mode (octal `0o666` by default), applied solely at the moment a database must be created.

Raises:

**error** – If an invalid *flag* argument is passed.

Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

`gdbm` objects act much like mutable [mappings](https://docs.python.org/3.14/glossary.html#term-mapping), although the `items()`, `values()`, `pop()`, `popitem()`, and `update()` methods are absent, `keys()` yields a list, and `setdefault()` needs two arguments. A “closing” context manager is also offered through the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword.

Changed in version 3.2: Added the `get()` and `setdefault()` methods.

Changed in version 3.13: Added the `clear()` method.

The following methods are also provided:

 gdbm.close()

Close the GDBM database.

 gdbm.firstkey()

Pairing this method with `nextkey()` lets you iterate across every key held in the database. Ordering follows GDBM’s internal hash values, so it isn’t sorted by the keys themselves. This method gives back the first key.

 gdbm.nextkey(*key*)

Returns the key that follows *key* in the traversal. The code below prints each key in the database `db` without needing to build a full in-memory list of them all:

```python
k = db.firstkey()
while k is not None:
    print(k)
    k = db.nextkey(k)

```

 gdbm.reorganize()

After performing many deletions, if you want to reclaim the space occupied by the GDBM file, this routine reorganizes the database. Apart from this reorganization, `gdbm` objects never trim a database file’s length; the space freed by deletions is otherwise retained and reused as fresh (key, value) pairs come in.

 gdbm.sync()

If the database was opened in fast mode, this method pushes any still-unwritten data out to the disk.

[Subject index](INDEX.md) · [Previous](dbm-gnu-error-to-dbm-gnu-open.md) · [Continue](../dbm-ndbm/dbm-ndbm-error-to-dbm-ndbm-open.md) · [Owning module, declaration or section: dbm.gnu](dbm-gnu-error-to-dbm-gnu-open.md)
