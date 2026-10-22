# Python 3.13.0 alpha 4 / library / termios

[gh-114492](https://github.com/python/cpython/issues/114492): Render the output of [`termios.tcgetattr()`](https://docs.python.org/3.14/library/termios.html#termios.tcgetattr) reproducible on Alpine Linux. Formerly some fields could be left holding random garbage.

[gh-85984](https://github.com/python/cpython/issues/85984): Brought `_POSIX_VDISABLE` over from C's `<unistd.h>` into [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
