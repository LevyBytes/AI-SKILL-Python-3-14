# Python 3.12.0 alpha 6 / library / pty

[gh-85984](https://github.com/python/cpython/issues/85984): Reworked the [`pty.fork()`](https://docs.python.org/3.14/library/pty.html#pty.fork) implementation to rely on [`os.login_tty()`](https://docs.python.org/3.14/library/os.html#os.login_tty).

A [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) now comes from `pty.master_open()` and `pty.slave_open()`. These were undocumented and were deprecated ages ago within the docstring, which steered users toward [`pty.openpty()`](https://docs.python.org/3.14/library/pty.html#pty.openpty) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
