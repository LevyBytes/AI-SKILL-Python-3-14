# Python 3.14.0 beta 1 / library / curses

[gh-133139](https://github.com/python/cpython/issues/133139): Introduce the [`curses.assume_default_colors()`](https://docs.python.org/3.14/library/curses.html#curses.assume_default_colors) function, a variant of the [`curses.use_default_colors()`](https://docs.python.org/3.14/library/curses.html#curses.use_default_colors) function that permits altering color pair `0`.

[bpo-44172](https://bugs.python.org/issue?@action=redirect&bpo=44172): A reference to the original [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) windows is now retained inside subwindows, preventing the parent window from being destroyed ahead of its subwindows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
