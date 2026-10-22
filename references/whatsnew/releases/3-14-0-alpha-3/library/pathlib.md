# Python 3.14.0 alpha 3 / library / pathlib

[gh-125413](https://github.com/python/cpython/issues/125413): Back out the `pathlib.Path.scandir()` addition. That method had landed in 3.14.0a2. Although the optimizations stay in place for file system paths, every other subclass now needs only to provide [`pathlib.Path.iterdir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.iterdir).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
