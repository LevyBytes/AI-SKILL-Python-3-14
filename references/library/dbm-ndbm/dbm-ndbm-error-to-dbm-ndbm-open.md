# dbm.ndbm — `dbm.ndbm` — New Database Manager

### `dbm.ndbm` — New Database Manager

**Source code:** [Lib/dbm/ndbm.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/ndbm.py)

---

The `dbm.ndbm` module wraps the NDBM library. You can drive it either through the “classic” NDBM interface or via the GDBM compatibility interface.

Note

Files written by `dbm.gnu` use a different format from those written by `dbm.ndbm`, so the two cannot be swapped for one another.

Warning

The version of the NDBM library bundled with macOS carries an undocumented cap on value size, so storing values above that cap can corrupt the database files. Reading back such corrupted files may trigger a hard crash (segmentation fault).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 *exception *dbm.ndbm.error

Raised for problems unique to `dbm.ndbm`, for example I/O errors. General mapping errors, such as supplying a bad key, raise [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) instead.

 dbm.ndbm.library

Name of the NDBM implementation library used.

 dbm.ndbm.open(*filename*, *flag='r'*, *mode=0o666*, */*)

Open an NDBM database and return an `ndbm` object.

Parameters:

- **filename** ([path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object)) – The basename of the database file (without the `.dir` or `.pag` extensions).

-

[Subject index](INDEX.md) · [Previous](../dbm-gnu/gdbm-close-to-gdbm-sync.md) · [Continue](ndbm-close.md)
