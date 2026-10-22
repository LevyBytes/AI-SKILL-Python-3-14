# exceptions C API: Windows, import and syntax exception construction

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetExcFromWindowsErr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, int ierr)

*Return value: Always NULL.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows as of version 3.7.*

Comparable to `PyErr_SetFromWindowsErr()`, with one extra parameter naming the exception type that should be raised.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetFromWindowsErrWithFilename(int ierr, const char *filename)

*Return value: Always NULL.** Included in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows from version 3.7 onward.*

Comparable to `PyErr_SetFromWindowsErr()`, with the extra behavior that whenever *filename* is not `NULL`, it is decoded from the filesystem encoding ([`os.fsdecode()`](https://docs.python.org/3.14/library/os.html#os.fsdecode)) and handed to the constructor of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) as a third parameter, to be used in defining the `filename` attribute on the exception instance.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetExcFromWindowsErrWithFilenameObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, int ierr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename)

*Return value: Always NULL.** On Windows, part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since release 3.7.*

Comparable to `PyErr_SetExcFromWindowsErr()`, with the extra behavior that whenever *filename* is not `NULL`, it is handed to the constructor of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) as a third parameter, to be used in defining the `filename` attribute on the exception instance.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetExcFromWindowsErrWithFilenameObjects([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, int ierr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename2)

*Return value: Always NULL.** A Windows member of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) beginning at version 3.7.*

Comparable to `PyErr_SetExcFromWindowsErrWithFilenameObject()`, but it takes a second filename object.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.4.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetExcFromWindowsErrWithFilename([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *type, int ierr, const char *filename)

*Return value: Always NULL.** On Windows it joined the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) at version 3.7.*

Comparable to `PyErr_SetFromWindowsErrWithFilename()`, with one extra parameter naming the exception type that should be raised.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetImportError([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *msg, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path)

*Return value: Always NULL.** Added to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) at release 3.7.*

This convenience function raises [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError). *msg* becomes the exception's message string. *name* and *path*, each of which may be `NULL`, become the `ImportError`'s respective `name` and `path` attributes.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyErr_SetImportErrorSubclass([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exception, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *msg, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) as of release 3.6.*

Very much like `PyErr_SetImportError()`, except this function lets you name a subclass of [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) to raise.

Added in version 3.6.

 void PyErr_SyntaxLocationObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, int lineno, int col_offset)

Record file, line, and offset information for the current exception. Should the current exception not be a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), then it sets extra attributes that lead the exception printing subsystem to treat the exception as a `SyntaxError`.

Added in version 3.4.

 void PyErr_RangedSyntaxLocationObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, int lineno, int col_offset, int end_lineno, int end_col_offset)

Comparable to `PyErr_SyntaxLocationObject()`, but it additionally records the *end_lineno* and *end_col_offset* information for the current exception.

Added in version 3.10.

 void PyErr_SyntaxLocationEx(const char *filename, int lineno, int col_offset)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Like `PyErr_SyntaxLocationObject()`, except *filename* is a byte string decoded from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

Added in version 3.2.

 void PyErr_SyntaxLocation(const char *filename, int lineno)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PyErr_SyntaxLocationEx()`, except the *col_offset* parameter is left out.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyerr-setstring-to-pyerr-setfromwindowserr.md) · [Following source contract](pyerr-badinternalcall-to-pyerr-programtext.md)
