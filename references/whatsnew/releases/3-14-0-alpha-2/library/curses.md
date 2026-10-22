# Python 3.14.0 alpha 2 / library / curses

[gh-126313](https://github.com/python/cpython/issues/126313): Repair a problem in [`curses.napms()`](https://docs.python.org/3.14/library/curses.html#curses.napms) triggered when [`curses.initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr) had not been invoked yet. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
