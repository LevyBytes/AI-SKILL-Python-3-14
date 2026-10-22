# dbm.gnu — `dbm.gnu` — GNU database manager

### `dbm.gnu` — GNU database manager

**Source code:** [Lib/dbm/gnu.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/gnu.py)

---

Like the `dbm.ndbm` module, the `dbm.gnu` module wraps the GDBM library, though it adds extras such as crash tolerance.

Note

Files written by `dbm.gnu` use a different format from those written by `dbm.ndbm`, so the two cannot be swapped for one another.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 *exception *dbm.gnu.error

Raised for problems unique to `dbm.gnu`, for example I/O errors. General mapping errors, such as supplying a bad key, raise [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) instead.

 dbm.gnu.open_flags

A string of characters the *flag* parameter of `open()` supports.

 dbm.gnu.open(*filename*, *flag='r'*, *mode=0o666*, */*)

Open a GDBM database and return a `gdbm` object.

Parameters:

- **filename** ([path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object)) – The database file to open.

-

[Subject index](INDEX.md) · [Previous](../dbm-sqlite3/sqlite3-close.md) · [Continue](gdbm-close-to-gdbm-sync.md)
