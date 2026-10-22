# Python 3.14.0 beta 1 / c api / ctypes

[gh-131747](https://github.com/python/cpython/issues/131747): Outside of Windows, relying on [`ctypes.Structure._pack_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._pack_) to request a Windows-style layout on those platforms is now deprecated. Make the layout explicit instead by assigning [`ctypes.Structure._layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_) the value `'ms'`.

[gh-132470](https://github.com/python/cpython/issues/132470): Constructing a [`ctypes.CField`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CField) whose *byte_size* fails to align with the real type size will now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), rather than crashing the interpreter as before.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
