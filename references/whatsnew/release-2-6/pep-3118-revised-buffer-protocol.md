# What’s New in Python 2.6 / PEP 3118: Revised Buffer Protocol — re

### PEP 3118: Revised Buffer Protocol

A C-level API, the buffer protocol lets Python types pass one another pointers into their internal storage. A memory-mapped file, for one, can be regarded as a buffer of characters, which permits a separate module such as [`re`](https://docs.python.org/3.14/library/re.html#module-re) to treat memory-mapped files as a string of characters open to searching.

Numeric-processing libraries like NumPy are the buffer protocol's chief consumers, since they reveal an array's internal layout so that callers may write data straight into the array rather than route it through a slower API. Drawing on lessons learned during NumPy development, this PEP revises the buffer protocol, introducing several new capabilities such as reporting an array's shape or pinning a region of memory.

The single most significant new C API function is `PyObject_GetBuffer(PyObject *obj, Py_buffer *view, int flags)`, which accepts an object plus a collection of flags and populates the `Py_buffer` structure with details about that object's memory layout. By means of this operation an object can pin its memory in place while an outside caller might be altering the contents, so a companion `PyBuffer_Release(Py_buffer *view)` exists to signal that the outside caller has finished.

Passing the *flags* argument to [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) lets you place constraints on the memory that comes back. A few illustrations:

- [`PyBUF_WRITABLE`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBUF_WRITABLE) signals that the memory has to be writable.

- `PyBUF_LOCK` asks for either a read-only or an exclusive lock over the memory.

- [`PyBUF_C_CONTIGUOUS`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBUF_C_CONTIGUOUS) and [`PyBUF_F_CONTIGUOUS`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBUF_F_CONTIGUOUS) ask for a layout that is either C-contiguous (the final dimension is the fastest-varying) or Fortran-contiguous (the leading dimension is the fastest-varying).

[`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) gains two fresh argument codes, `s*` and `z*`, which hand back locked buffer objects for a parameter.

See also

[**PEP 3118**](https://peps.python.org/pep-3118/) - Revising the buffer protocol

PEP written by Travis Oliphant and Carl Banks; implemented by Travis Oliphant.

[Subject index](INDEX.md) · [Previous source section](pep-3116-new-i-o-library.md) · [Release/subject declaration](python-3-0.md) · [Next source section](abstract-base-class-protocols.md)
