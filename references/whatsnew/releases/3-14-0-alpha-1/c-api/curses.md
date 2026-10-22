# Python 3.14.0 alpha 1 / c api / curses

[gh-123961](https://github.com/python/cpython/issues/123961): Turn the [curses.window](https://docs.python.org/3.14/library/curses.html#curses-window-objects) static type that the `PyCursesWindow_Type` macro exposes in `Include/py_curses.h` into a [heap type](https://docs.python.org/3.14/c-api/typeobj.html#heap-types). Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
