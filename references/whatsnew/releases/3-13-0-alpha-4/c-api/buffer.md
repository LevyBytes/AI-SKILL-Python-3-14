# Python 3.13.0 alpha 4 / c api / buffer

[gh-114685](https://github.com/python/cpython/issues/114685): [`PyBuffer_FillInfo()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FillInfo) now throws a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) once invoked with [`PyBUF_READ`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyBUF_READ) or [`PyBUF_WRITE`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyBUF_WRITE) given as flags. Those flags belong solely with the `PyMemoryView_*` C API.

[gh-114685](https://github.com/python/cpython/issues/114685): [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) now throws a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) once invoked with [`PyBUF_READ`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyBUF_READ) or [`PyBUF_WRITE`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyBUF_WRITE) given as flags. Those flags belong solely with the `PyMemoryView_*` C API.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
