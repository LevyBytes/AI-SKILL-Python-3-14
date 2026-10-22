# dbm.sqlite3 — `dbm.sqlite3` — SQLite backend for dbm

### `dbm.sqlite3` — SQLite backend for dbm

Added in version 3.13.

**Source code:** [Lib/dbm/sqlite3.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/sqlite3.py)

---

By drawing on the standard library [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module, this module supplies an SQLite backend for `dbm`. Files produced by `dbm.sqlite3` are therefore openable with `sqlite3`, with any other SQLite browser, or with the SQLite CLI.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

 dbm.sqlite3.open(*filename*, */*, *flag='r'*, *mode=0o666*)

Open an SQLite database.

Parameters:

- **filename** ([path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object)) – The path to the database to be opened.

-

[Subject index](INDEX.md) · [Previous](../dbm/flag-str.md) · [Continue](sqlite3-close.md)
