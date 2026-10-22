# Printing and clearing

### Printing and clearing

 void PyErr_Clear()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Clear the error indicator. When the error indicator is unset, nothing happens.

 void PyErr_PrintEx(int set_sys_last_vars)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Write a standard traceback to `sys.stderr` and clear the error indicator. **Unless** the error happens to be a `SystemExit`, in which case no traceback is emitted and the Python process exits using the error code carried by the `SystemExit` instance.

Invoke this function **only** while the error indicator is set. Doing otherwise triggers a fatal error!

When *set_sys_last_vars* is nonzero, the printed exception is assigned to the variable [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc). To preserve backwards compatibility, the deprecated variables [`sys.last_type`](https://docs.python.org/3.14/library/sys.html#sys.last_type), [`sys.last_value`](https://docs.python.org/3.14/library/sys.html#sys.last_value) and [`sys.last_traceback`](https://docs.python.org/3.14/library/sys.html#sys.last_traceback) likewise receive the type, value and traceback of this exception, respectively.

Changed in version 3.12: The setting of [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc) was added.

 void PyErr_Print()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Alias for `PyErr_PrintEx(1)`.

 void PyErr_WriteUnraisable([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) with the current exception and the *obj* argument.

This helper function emits a warning message to `sys.stderr` whenever an exception has been set but the interpreter has no way to actually raise it. One example of its use is when an exception arises within a [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method.

A single argument *obj* is passed to the function to identify the context where the unraisable exception came up. Where feasible, the warning message will include the repr of *obj*. When *obj* is `NULL`, the warning shows only the traceback.

Calling this function requires that an exception be set.

Changed in version 3.4: A traceback is now printed; when *obj* is `NULL`, the traceback alone appears.

Changed in version 3.8: Use [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook).

 void PyErr_FormatUnraisable(const char *format, ...)

Comparable to `PyErr_WriteUnraisable()`, except the *format* plus the following parameters serve to format the warning message; their meaning and values match those of [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat). `PyErr_WriteUnraisable(obj)` corresponds roughly to `PyErr_FormatUnraisable("Exception ignored in: %R", obj)`. When *format* is `NULL`, only the traceback appears.

Added in version 3.13.

 void PyErr_DisplayException([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Emit the standard traceback display of `exc` to `sys.stderr`, with chained exceptions and notes included.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous source contract](exception-handling.md) · [Following source contract](pyerr-setstring-to-pyerr-setfromwindowserr.md)
