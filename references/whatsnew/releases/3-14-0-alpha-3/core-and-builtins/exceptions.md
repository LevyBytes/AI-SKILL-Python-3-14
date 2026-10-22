# Python 3.14.0 alpha 3 / core and builtins / exceptions

[gh-127651](https://github.com/python/cpython/issues/127651): For absent symbols in `from` imports that raise [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError), the message now falls back to `__file__` whenever `__spec__.origin` does not denote a location

[gh-126937](https://github.com/python/cpython/issues/126937): Resolve the [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) raised when a [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) field has a size exceeding an unsigned 16-bit integer. The ceiling on *bits* is now [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
