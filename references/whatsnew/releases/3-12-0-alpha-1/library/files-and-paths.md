# Python 3.12.0 alpha 1 / library / files and paths

[gh-97930](https://github.com/python/cpython/issues/97930): Brings in the importlib_resources 5.8 and 5.9 changes: `Traversable.joinpath` now ships a concrete implementation, and `as_file` gains support for directories of resources.

[gh-46412](https://github.com/python/cpython/issues/46412): `bool(db)` runs faster against large ndb/gdb databases. The old path invoked `len(db)`, which walked every key – yet whether a database is empty or not becomes clear once the very first key appears.

[gh-94214](https://github.com/python/cpython/issues/94214): The `context` object that the `venv.EnvBuilder` class uses is documented, and the freshly created environment's library path is appended to it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
