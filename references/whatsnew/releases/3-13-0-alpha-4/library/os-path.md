# Python 3.13.0 alpha 4 / library / os path

[gh-88569](https://github.com/python/cpython/issues/88569): Introduce [`os.path.isreserved()`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved), a function that flags reserved pathnames like "NUL", "AUX" and "CON". It exists on Windows only.

Mark [`pathlib.PurePath.is_reserved()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_reserved) as deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
