# Python 3.11.0 alpha 4 / c api / buffer

[bpo-46140](https://bugs.python.org/issue?@action=redirect&bpo=46140): [`PyBuffer_GetPointer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_GetPointer), [`PyBuffer_FromContiguous()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FromContiguous), [`PyBuffer_ToContiguous()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_ToContiguous) and [`PyMemoryView_FromBuffer()`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyMemoryView_FromBuffer) now accept buffer info through `const Py_buffer *` in place of `Py_buffer *`, since mutability is unnecessary. Additionally `PyBuffer_FromContiguous()` now receives the source buffer as `const void *`, and likewise `PyBuffer_GetPointer()` receives the strides as `const Py_ssize_t *`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
