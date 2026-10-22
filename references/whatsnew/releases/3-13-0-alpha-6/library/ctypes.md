# Python 3.13.0 alpha 6 / library / ctypes

[gh-114314](https://github.com/python/cpython/issues/114314): In [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes), ctype data now lives directly on type objects rather than inside a dict subclass. That is an internal tweak that ought not change how you use it.

[gh-71052](https://github.com/python/cpython/issues/71052): Provide an Android implementation of [`ctypes.util.find_library()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.find_library).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
