# Python 3.13.0 alpha 2 / library / tty

[gh-110392](https://github.com/python/cpython/issues/110392): Correct [`tty.setraw()`](https://docs.python.org/3.14/library/tty.html#tty.setraw) and [`tty.setcbreak()`](https://docs.python.org/3.14/library/tty.html#tty.setcbreak), which formerly handed back a partially altered list of the original tty attributes. Both [`tty.cfmakeraw()`](https://docs.python.org/3.14/library/tty.html#tty.cfmakeraw) and [`tty.cfmakecbreak()`](https://docs.python.org/3.14/library/tty.html#tty.cfmakecbreak) now copy the special-character list prior to changing it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
