# exceptions C API: `PyErr_WarnFormat()`, `PyErr_WarnExplicitFormat()`, `PyErr_ResourceWarning()`

int PyErr_WarnFormat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *category, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) stack_level, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyErr_WarnEx()`, except the warning text is built through [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat). Here *format* is an ASCII-encoded string.

Added in version 3.2.

 int PyErr_WarnExplicitFormat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *category, const char *filename, int lineno, const char *module, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *registry, const char *format, ...)

Behaves like `PyErr_WarnExplicit()`, except the warning text is built through [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat). Here *format* is an ASCII-encoded string.

Added in version 3.2.

 int PyErr_ResourceWarning([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *source, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) stack_level, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.6.*

Behaves like `PyErr_WarnFormat()`, except that *category* is fixed to [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) and that *source* is handed off to `warnings.WarningMessage`.

Added in version 3.6.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyerr-warnex-to-pyerr-warnexplicit.md) · [Following source contract](pyerr-occurred-to-pyerr-setraisedexception.md)
