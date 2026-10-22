# Python 3.13.0 alpha 4 / library / tty

[gh-114328](https://github.com/python/cpython/issues/114328): Neither [`tty.setcbreak()`](https://docs.python.org/3.14/library/tty.html#tty.setcbreak) nor the new [`tty.cfmakecbreak()`](https://docs.python.org/3.14/library/tty.html#tty.cfmakecbreak) wipes the terminal input ICRLF flag any longer. That corrects a regression brought in with 3.12 which stopped matching the way operating systems describe cbreak mode in their `stty(1)` manual pages.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
