# Python 3.14.0 beta 2 / library / curses

[gh-134209](https://github.com/python/cpython/issues/134209): [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses): The [`curses.window.instr()`](https://docs.python.org/3.14/library/curses.html#curses.window.instr) and [`curses.window.getstr()`](https://docs.python.org/3.14/library/curses.html#curses.window.getstr) methods now place their internal buffer on the heap rather than the stack; additionally, the maximum buffer size grows from 1023 to 2047.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
