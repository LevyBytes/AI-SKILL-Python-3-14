# Python 3.14.0 alpha 6 / library / pathlib

[gh-130608](https://github.com/python/cpython/issues/130608): Drops the *dirs_exist_ok* argument out of [`pathlib.Path.copy()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy) plus [`copy_into()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy_into). Both methods arrive fresh in Python 3.14.

[gh-125413](https://github.com/python/cpython/issues/125413): Guarantees the path handed back from [`pathlib.Path.copy()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy) or [`move()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.move) carries fresh [`info`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.info).

[gh-125413](https://github.com/python/cpython/issues/125413): Makes [`Path.copy`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.copy) quicker by leaning on [`info`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.info) more effectively under the hood.

[gh-128520](https://github.com/python/cpython/issues/128520): Applies type conversion uniformly so that [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) methods will take a path object as an argument, [`match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.match) and [`rename()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rename) among them. That argument now becomes a path object when it has no [`with_segments()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_segments) attribute, and otherwise stays as is.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
