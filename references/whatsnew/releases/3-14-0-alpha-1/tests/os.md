# Python 3.14.0 alpha 1 / tests / os

[gh-99242](https://github.com/python/cpython/issues/99242): Under some conditions (chroot being one example), [`os.getloadavg()`](https://docs.python.org/3.14/library/os.html#os.getloadavg) can raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) while regression tests run. That error is henceforth trapped and disregarded, because reporting the load average is optional.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
