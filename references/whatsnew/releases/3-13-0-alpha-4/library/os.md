# Python 3.13.0 alpha 4 / library / os

[gh-85984](https://github.com/python/cpython/issues/85984): Provide the POSIX pseudo-terminal functions [`os.posix_openpt()`](https://docs.python.org/3.14/library/os.html#os.posix_openpt), [`os.grantpt()`](https://docs.python.org/3.14/library/os.html#os.grantpt), [`os.unlockpt()`](https://docs.python.org/3.14/library/os.html#os.unlockpt), and [`os.ptsname()`](https://docs.python.org/3.14/library/os.html#os.ptsname).

[gh-102512](https://github.com/python/cpython/issues/102512): Whenever [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) is invoked from a foreign thread (that is, a `_DummyThread`), the thread's type inside the child process becomes `_MainThread`. Its name and daemonic flag were changed too, and it can now be joined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
