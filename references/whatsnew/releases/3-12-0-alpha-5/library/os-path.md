# Python 3.12.0 alpha 5 / library / os path

[gh-101000](https://github.com/python/cpython/issues/101000): Provide [`os.path.splitroot()`](https://docs.python.org/3.14/library/os.path.html#os.path.splitroot), splitting a path into the 3-item tuple `(drive, root, tail)`. [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) now leans on this new function so that path construction runs as much as a third quicker.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
