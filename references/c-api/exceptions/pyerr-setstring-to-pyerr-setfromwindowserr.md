# exceptions C API: Setting thread errors and translating operating-system failures

### Raising exceptions

These functions assist you in setting the current thread's error indicator. As a convenience, several of them always hand back a `NULL` pointer suitable for use within a `return` statement.

 void PyErr_SetString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, const char *message)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is the most usual approach to setting the error indicator. The first argument names the exception type; ordinarily one of the standard exceptions, such as `PyExc_RuntimeError`. There is no need to make a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to it (for example via [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF)). The second argument carries an error message, decoded from `'utf-8'`.

 void PyErr_SetObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This function resembles `PyErr_SetString()`, but it permits you to supply any Python object as the "value" of the exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_Format([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exception, const char *format, ...)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This function sets the error indicator and yields `NULL`. *exception* ought to be a Python exception class. The *format* together with the subsequent parameters serve to format the error message; their meaning and values are identical to those in [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat). *format* is an ASCII-encoded string.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_FormatV([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exception, const char *format, va_list vargs)

*Return value: Always NULL.** Joined the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) at version 3.5.*

Identical to `PyErr_Format()`, except it accepts a `va_list` argument in place of a variable number of arguments.

Added in version 3.5.

 void PyErr_SetNone([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a shorthand for `PyErr_SetObject(type, Py_None)`.

 int PyErr_BadArgument()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a shorthand for `PyErr_SetString(PyExc_TypeError, message)`, in which *message* signals that a built-in operation was called with an illegal argument. Its purpose is chiefly internal.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_NoMemory()

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a shorthand for `PyErr_SetNone(PyExc_MemoryError)`; since it gives back `NULL`, an object allocation function can write `return PyErr_NoMemory();` upon exhausting its memory.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromErrno([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This convenience function raises an exception after a C library function has signaled an error by setting the C variable `errno`. It builds a tuple object whose first element is the integer `errno` value and whose second element is the matching error message (obtained via `strerror()`), then calls `PyErr_SetObject(type, object)`. On Unix, should the `errno` value equal `EINTR`, marking an interrupted system call, the function calls `PyErr_CheckSignals()`, and if that set the error indicator, it leaves the indicator set to that. Because the function always gives back `NULL`, a wrapper around a system call may write `return PyErr_SetFromErrno(type);` when its system call reports an error.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromErrnoWithFilenameObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filenameObject)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Comparable to `PyErr_SetFromErrno()`, with the extra behavior that whenever *filenameObject* is not `NULL`, it is handed to the constructor of *type* as a third parameter. For an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception, this serves to define the `filename` attribute on the exception instance.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromErrnoWithFilenameObjects([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filenameObject, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filenameObject2)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Comparable to `PyErr_SetFromErrnoWithFilenameObject()`, but it accepts a second filename object, useful for raising errors when a function taking two filenames fails.

Added in version 3.4.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromErrnoWithFilename([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, const char *filename)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Comparable to `PyErr_SetFromErrnoWithFilenameObject()`, except the filename arrives as a C string. *filename* is decoded using the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromWindowsErr(int ierr)

*Return value: Always NULL.** On Windows, a member of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) starting with version 3.7.*

This convenience function raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). When called with *ierr* equal to `0`, the error code from a call to `GetLastError()` is substituted. It invokes the Win32 function `FormatMessage()` to fetch the Windows description for the error code supplied by *ierr* or `GetLastError()`, then it builds an `OSError` object whose [`winerror`](https://docs.python.org/3.14/library/exceptions.html#OSError.winerror) attribute holds the error code and whose [`strerror`](https://docs.python.org/3.14/library/exceptions.html#OSError.strerror) attribute holds the matching error message (taken from `FormatMessage()`), and then calls `PyErr_SetObject(PyExc_OSError, object)`. This function always gives back `NULL`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

[Subject index](INDEX.md) · [Previous source contract](pyerr-clear-to-pyerr-displayexception.md) · [Following source contract](pyerr-setexcfromwindowserr-to-pyerr-syntaxlocation.md)
