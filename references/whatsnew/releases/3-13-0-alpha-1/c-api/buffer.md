# Python 3.13.0 alpha 1 / c api / buffer

[gh-85275](https://github.com/python/cpython/issues/85275): `PyObject_AsCharBuffer()`, `PyObject_AsReadBuffer()`, `PyObject_CheckReadBuffer()`, and `PyObject_AsWriteBuffer()` are removed. Move over to the new buffer protocol; [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) and [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
