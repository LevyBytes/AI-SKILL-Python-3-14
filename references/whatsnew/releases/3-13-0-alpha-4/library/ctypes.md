# Python 3.13.0 alpha 4 / library / ctypes

[gh-114257](https://github.com/python/cpython/issues/114257): Swallow the `FileNotFound` error inside [`ctypes.util.find_library()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.find_library) and simply hand back `None` under Linux.

[gh-105102](https://github.com/python/cpython/issues/105102): Permit a [`ctypes.Union`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Union) to nest within a [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) even where the system endianness runs opposite to that of the classes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
