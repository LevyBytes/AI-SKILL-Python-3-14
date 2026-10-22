# Python 3.12.0 beta 1 / library / tty

[gh-85984](https://github.com/python/cpython/issues/85984): Add [`tty.cfmakeraw()`](https://docs.python.org/3.14/library/tty.html#tty.cfmakeraw) along with [`tty.cfmakecbreak()`](https://docs.python.org/3.14/library/tty.html#tty.cfmakecbreak) to [`tty`](https://docs.python.org/3.14/library/tty.html#module-tty) and bring [`tty.setraw()`](https://docs.python.org/3.14/library/tty.html#tty.setraw) and [`tty.setcbreak()`](https://docs.python.org/3.14/library/tty.html#tty.setcbreak) up to date so their default behaviour uses the POSIX.1-2017 Chapter 11 "General Terminal Interface" flag masks.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
