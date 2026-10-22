# Python 3.12.0 alpha 1 / windows / os

[gh-43414](https://github.com/python/cpython/issues/43414): [`os.get_terminal_size()`](https://docs.python.org/3.14/library/os.html#os.get_terminal_size) will now try to obtain the size from whatever handle you hand it, instead of working only with file descriptors 0, 1 and 2.

[gh-97728](https://github.com/python/cpython/issues/97728): Stops potential crashes that stemmed from reading uninitialized variables when bad arguments reach [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) on Windows and certain Windows-only modules (such as `winreg`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
