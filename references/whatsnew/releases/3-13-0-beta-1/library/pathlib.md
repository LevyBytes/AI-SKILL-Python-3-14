# Python 3.13.0 beta 1 / library / pathlib

[gh-112855](https://github.com/python/cpython/issues/112855): Accelerates pickling of [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) objects. Barney Gale wrote the patch.

[gh-115060](https://github.com/python/cpython/issues/115060): Accelerates [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) by skipping an initial [`is_dir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_dir) call. Because of this, `glob()` is no longer capable of raising [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[gh-115060](https://github.com/python/cpython/issues/115060): Accelerates [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) by skipping directory scans for pattern segments that contain no wildcards.

[gh-117727](https://github.com/python/cpython/issues/117727): Accelerates [`pathlib.Path.iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir) through internal use of [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir).

[gh-117586](https://github.com/python/cpython/issues/117586): Accelerates [`pathlib.Path.walk()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.walk) by operating on strings under the hood.

[gh-117586](https://github.com/python/cpython/issues/117586): Accelerates [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) by operating on strings under the hood.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
