# Python 3.13.0 alpha 4 / library / pathlib

[gh-79634](https://github.com/python/cpython/issues/79634): Take [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) as patterns within [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob).

[gh-115060](https://github.com/python/cpython/issues/115060): Make [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) faster by dropping superfluous regex matching.

[gh-70303](https://github.com/python/cpython/issues/70303): Hand back files together with directories from [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) whenever a pattern closes with "`**`". Formerly the call yielded directories alone.

[gh-113225](https://github.com/python/cpython/issues/113225): Accelerate [`pathlib.Path.walk()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.walk) by leaning on [`os.DirEntry.path`](https://docs.python.org/3.14/library/os.html#os.DirEntry.path) wherever feasible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
