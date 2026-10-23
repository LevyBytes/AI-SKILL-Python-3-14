# dbm`dbm` - Interfaces to Unix “databases”

# Dbm, Debug

## Overview

Covers: dbm — Interfaces to Unix “databases”; Debugging and Profiling.

## dbm - Interfaces to Unix “databases”

### `dbm` - Interfaces to Unix “databases”

**Source code:** [Lib/dbm/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/__init__.py)

---

`dbm` exposes a common interface that wraps several flavors of the DBM database:

- `dbm.sqlite3`

- `dbm.gnu`

- `dbm.ndbm`

When none of those modules are present, `dbm` falls back to the basic-but-sluggish `dbm.dumb` implementation. A [third party interface](https://www.jcea.es/programacion/pybsddb.htm) also exists for the Oracle Berkeley DB.

 *exception *dbm.error

A tuple holding the exceptions each supported module may raise, where the first entry is a distinct exception that is likewise named `dbm.error` — that first one is what gets raised when `dbm.error` is raised.

 dbm.whichdb(*filename*)

Given a file, this function tries to work out which of the available simple database modules — `dbm.sqlite3`, `dbm.gnu`, `dbm.ndbm`, or `dbm.dumb` — is suitable for opening it.

One of these values is returned:

- `None` when the file is unreadable or absent and therefore cannot be opened

- an empty string (`''`) when the file’s format is not recognizable

- a string holding the name of the needed module, for instance `'dbm.ndbm'` or `'dbm.gnu'`

Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 dbm.open(*file*, *flag='r'*, *mode=0o666*)

Open a database and return the corresponding database object.

Parameters:

- **file** ([path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object)) –

The database file to open.

When the database file is already present, `whichdb()` identifies its type so the matching module can be selected; when it is absent, the first of the submodules listed above that can be imported is chosen.

-

[Subject index](INDEX.md) · [Continue](flag-str.md)
