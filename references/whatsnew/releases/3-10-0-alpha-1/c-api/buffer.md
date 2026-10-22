# Python 3.10.0 alpha 1 / c api / buffer

[bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103): The `PyObject_AsCharBuffer()`, `PyObject_AsReadBuffer()`, `PyObject_CheckReadBuffer()`, and `PyObject_AsWriteBuffer()` calls are gone. Move over to the new buffer protocol: [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) and [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
