# Python 3.14.5 release candidate 1 / documentation / glob

[gh-146646](https://github.com/python/cpython/issues/146646): Note that [`glob.glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob), [`glob.iglob()`](https://docs.python.org/3.14/library/glob.html#glob.iglob), [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob), and [`pathlib.Path.rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) quietly swallow any [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) thrown while walking the filesystem.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
