# Python 3.14.0 alpha 1 / library / curses

[gh-123961](https://github.com/python/cpython/issues/123961): Moves [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) over to multi-phase initialization ([**PEP 489**](https://peps.python.org/pep-0489/)), which clears up reference leaks during interpreter teardown. Bénédikt Tran wrote the patch.

[gh-120378](https://github.com/python/cpython/issues/120378): Eliminates a crash tied to integer overflow within [`curses.resizeterm()`](https://docs.python.org/3.14/library/curses.html#curses.resizeterm) and [`curses.resize_term()`](https://docs.python.org/3.14/library/curses.html#curses.resize_term).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
