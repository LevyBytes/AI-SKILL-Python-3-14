# Python 3.14.0 alpha 1 / library / files and paths

[gh-120910](https://github.com/python/cpython/issues/120910): While reading installed files out of an egg, apply `relative_to(walk_up=True)` so files placed outside the installation root are respected.

[gh-120678](https://github.com/python/cpython/issues/120678): Repair a regression in the new REPL where globals coming from files supplied through the `-i` argument were left out of the REPL's global namespace. Patch by Alex Waygood.

[gh-122903](https://github.com/python/cpython/issues/122903): `zipfile.Path.glob` will now match directories properly rather than quietly dropping them.

[gh-121245](https://github.com/python/cpython/issues/121245): Repair a defect in the command-history handling of the new [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) that erased the history file when the REPL exited.

[gh-120754](https://github.com/python/cpython/issues/120754): `Pathlib.read_bytes` now skips Python's buffered I/O mode when opening the file. Since the routine reads the whole file at once, this trims overhead and yields a modest speedup.

[gh-119588](https://github.com/python/cpython/issues/119588): `zipfile.Path.is_symlink` now determines whether the supplied path is a symlink.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
