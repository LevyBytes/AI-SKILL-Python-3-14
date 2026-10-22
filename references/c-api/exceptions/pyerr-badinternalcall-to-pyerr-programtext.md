# exceptions C API: `PyErr_BadInternalCall()`, `PyErr_ProgramTextObject()`, `PyErr_ProgramText()`

void PyErr_BadInternalCall()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a shorthand for `PyErr_SetString(PyExc_SystemError, message)`, in which *message* signals that an internal operation (for instance a Python/C API function) was called with an illegal argument. Its purpose is chiefly internal.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_ProgramTextObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, int lineno)

Fetch, from within *filename*, the source line numbered *lineno*. A Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object is what *filename* should be.

When it succeeds, this function gives back a Python string object holding the found line. When it fails, this function gives back `NULL` with no exception set.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_ProgramText(const char *filename, int lineno)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Comparable to `PyErr_ProgramTextObject()`, except *filename* is a const char*, which is decoded using the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler), rather than a Python object reference.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyerr-setstring-to-pyerr-setfromwindowserr.md) · [Previous source contract](pyerr-setexcfromwindowserr-to-pyerr-syntaxlocation.md) · [Following source contract](pyerr-warnex-to-pyerr-warnexplicit.md)
