# Python 3.13.0 alpha 1 / library / pathlib

[gh-83863](https://github.com/python/cpython/issues/83863): Dropped the ability to treat [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects as context managers. Prior to Python 3.9, leaving the context manager tagged a path as "closed", after which some — though not every — method would raise upon being called. From Python 3.9 onward, using a path this way has no effect at all.

[gh-102613](https://github.com/python/cpython/issues/102613): Sped up [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) when a pattern carries a non-terminal "`**`" component, achieved by running walked paths through a regular expression rather than invoking [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) repeatedly on any single directory.

[gh-104996](https://github.com/python/cpython/issues/104996): Sped up [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) construction by postponing the joining of paths whenever several arguments arrive.

[gh-104947](https://github.com/python/cpython/issues/104947): Made comparisons among [`pathlib.PureWindowsPath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PureWindowsPath) objects behave the same on Windows and Posix, matching how 3.11 acted.

[gh-77609](https://github.com/python/cpython/issues/77609): Gave [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob) a *follow_symlinks* argument whose default is false.

[gh-73435](https://github.com/python/cpython/issues/73435): Added recursive-wildcard handling to [`pathlib.PurePath.match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.match).

[gh-109187](https://github.com/python/cpython/issues/109187): [`pathlib.Path.resolve()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.resolve) now handles symlink loops just like any other error: under strict mode an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised, while under non-strict mode nothing is raised.

[gh-89812](https://github.com/python/cpython/issues/89812): Introduce [`pathlib.UnsupportedOperation`](https://docs.python.org/3.14/library/pathlib.html#pathlib.UnsupportedOperation), thrown in place of [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) whenever a path operation isn't supported.

[gh-105793](https://github.com/python/cpython/issues/105793): Supply a *follow_symlinks* keyword-only argument on [`pathlib.Path.is_dir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_dir) and [`is_file()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_file), where the default is `True`.

[gh-110488](https://github.com/python/cpython/issues/110488): Resolved a pair of problems in [`pathlib.PurePath.with_name()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_name): a lone dot used to be accepted as a legitimate name, and under `PureWindowsPath` a name carrying an NTFS alternate data stream — for instance `a:b` — was wrongly treated as invalid.

[gh-106330](https://github.com/python/cpython/issues/106330): Correct the wrong matching of empty paths inside [`pathlib.PurePath.match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.match). The bug arrived with Python 3.12.0 beta 1.

[gh-107465](https://github.com/python/cpython/issues/107465): Introduce the [`pathlib.Path.from_uri()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.from_uri) classmethod.

[gh-78722](https://github.com/python/cpython/issues/78722): Resolve a problem where [`pathlib.Path.iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir) held off on raising [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) until it was iterated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
