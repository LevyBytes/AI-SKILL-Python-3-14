# Python 3.12.0 alpha 4 / library / pathlib

[gh-100562](https://github.com/python/cpython/issues/100562): Make [`pathlib.Path.absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.absolute) roughly twice as fast. The tradeoff is a slowdown in [`pathlib.Path.cwd()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.cwd), which user code tends to call less often.

[gh-78707](https://github.com/python/cpython/issues/78707): Passing more than one positional argument to [`pathlib.PurePath.relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.relative_to) and [`is_relative_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_relative_to) is now deprecated.

[bpo-24132](https://bugs.python.org/issue?@action=redirect&bpo=24132): Allow [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) to be subclassed (private for now). Earlier, trying to instantiate a subclass produced an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). Barney Gale wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
