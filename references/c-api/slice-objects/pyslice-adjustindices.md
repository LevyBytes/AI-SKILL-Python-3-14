# Py_ssize_t PySlice_AdjustIndices(Py_ssize_t length, Py_ssize_t *start, Py_ssize_t *stop, Py_ssize_t step)

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PySlice_AdjustIndices([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *stop, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) step)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Tune the start/end slice indices presuming a sequence of the given length. Indices that fall out of bounds get clipped in a way that lines up with how ordinary slices are handled.

Yield the length of the slice. Never fails. Runs no Python code.

Added in version 3.6.1.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyslice-type-to-pyslice-unpack.md) · [Following source contract](pyellipsis-type-to-py-ellipsis.md)
