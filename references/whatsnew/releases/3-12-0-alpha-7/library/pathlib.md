# Python 3.12.0 alpha 7 / library / pathlib

[bpo-36305](https://bugs.python.org/issue?@action=redirect&bpo=36305): Within [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib), correct how Windows filenames that look like drives, for instance `./a:b`, are handled.

[gh-76846](https://github.com/python/cpython/issues/76846): Fix a situation where the `__new__()` and `__init__()` methods on subclasses of [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) went uncalled under certain conditions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
