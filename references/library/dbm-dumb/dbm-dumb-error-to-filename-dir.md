# dbm.dumb`dbm.dumb` - Portable DBM implementation

### `dbm.dumb` - Portable DBM implementation

**Source code:** [Lib/dbm/dumb.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/dumb.py)

Note

Think of the `dbm.dumb` module as the `dbm` module’s final fallback for when no sturdier module is around. The `dbm.dumb` module wasn’t built for speed and sees far less use than the other database modules.

---

The `dbm.dumb` module supplies a persistent [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)-style interface coded purely in Python. In contrast to other `dbm` backends such as `dbm.gnu`, it depends on no external library.

The `dbm.dumb` module defines the following:

 *exception *dbm.dumb.error

Raised for problems unique to `dbm.dumb`, for example I/O errors. General mapping errors, such as supplying a bad key, raise [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) instead.

 dbm.dumb.open(*filename*, *flag='c'*, *mode=0o666*)

Open a `dbm.dumb` database.

Parameters:

- **filename** –

The database file’s basename, leaving off any extensions. When a database is freshly made, these files are produced:

  - `*filename*.dat`

  - `*filename*.dir`

-

[Subject index](INDEX.md) · [Previous](../dbm-ndbm/ndbm-close.md) · [Continue](dumbdbm-close-to-dumbdbm-sync.md)
