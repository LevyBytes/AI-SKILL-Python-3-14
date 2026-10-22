# Buffer-related functions

### Buffer-related functions

 int PyObject_CheckBuffer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Return `1` when *obj* supports the buffer interface, and `0` otherwise. A returned `1` does not promise that `PyObject_GetBuffer()` will succeed. This function never fails.

 int PyObject_GetBuffer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exporter, Py_buffer *view, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Issue a request to *exporter* asking it to fill in *view* as directed by *flags*. Should the exporter be unable to supply a buffer of precisely that type, it MUST raise [`BufferError`](https://docs.python.org/3.14/library/exceptions.html#BufferError), assign `NULL` to `view->obj`, and return `-1`.

When it succeeds, fill in *view*, assign `view->obj` a new reference to *exporter*, and return 0. Where chained buffer providers forward requests to one object, `view->obj` MAY point at that object rather than *exporter* (See [Buffer Object Structures](https://docs.python.org/3.14/c-api/typeobj.html#buffer-structs)).

Each successful call to `PyObject_GetBuffer()` must be matched by a call to `PyBuffer_Release()`, much as `malloc()` is matched with `free()`. So once the consumer has finished with the buffer, `PyBuffer_Release()` must be invoked exactly once.

 void PyBuffer_Release(Py_buffer *view)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Release the buffer *view* and give up the [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) (that is, decrement the reference count) to the view's backing object, `view->obj`. This function MUST be invoked once the buffer is no longer in use; failing to do so may cause reference leaks.

Calling this function on a buffer not obtained through `PyObject_GetBuffer()` is an error.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyBuffer_SizeFromFormat(const char *format)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Return the `itemsize` implied by `format`. On error, raise an exception and return -1.

Added in version 3.9.

 int PyBuffer_IsContiguous(const Py_buffer *view, char order)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Return `1` when the memory that *view* describes is [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous) in C-style layout (*order* set to `'C'`), in Fortran-style layout (*order* set to `'F'`), or in either layout (*order* set to `'A'`). Return `0` in all other cases. This function never fails.

 void *PyBuffer_GetPointer(const Py_buffer *view, const [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *indices)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Fetch the memory area that *indices* points to inside the supplied *view*. *indices* must point at an array holding `view->ndim` indices.

 int PyBuffer_FromContiguous(const Py_buffer *view, const void *buf, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len, char fort)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Copy contiguous *len* bytes out of *buf* into *view*. For *fort*, pass `'C'` to select C-style ordering or `'F'` for Fortran-style ordering. On success `0` comes back; an error yields `-1`.

 int PyBuffer_ToContiguous(void *buf, const Py_buffer *src, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len, char order)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Copy *len* bytes out of *src* into its contiguous representation in *buf*. For *order*, choose `'C'`, `'F'`, or `'A'` (selecting C-style ordering, Fortran-style ordering, or whichever applies). On success `0` comes back; an error yields `-1`.

This function fails if *len* != *src->len*.

 int PyObject_CopyData([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *dest, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *src)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Copy data out of the *src* buffer into the *dest* buffer. Conversion between C-style and Fortran-style buffers is possible.

`0` is returned on success, `-1` on error.

 void PyBuffer_FillContiguousStrides(int ndims, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *shape, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *strides, int itemsize, char order)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.11.*

Populate the *strides* array with the byte-strides of a [contiguous](https://docs.python.org/3.14/glossary.html#term-contiguous) array (C-style when *order* is `'C'`, or Fortran-style when *order* is `'F'`) having the given shape and the given count of bytes per element.

[Subject index](INDEX.md) · [Previous source contract](pil-style-shape-strides-and-suboffsets.md) · [Following source contract](pybuffer-fillinfo.md)
