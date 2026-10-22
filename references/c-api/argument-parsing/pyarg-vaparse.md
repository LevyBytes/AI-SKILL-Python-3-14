# int PyArg_VaParse(PyObject *args, const char *format, va_list vargs)

int PyArg_VaParse([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, const char *format, va_list vargs)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves just like `PyArg_ParseTuple()`, the one difference being that it takes a va_list in place of a variadic argument list.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyarg-parsetuple.md) · [Following source contract](pyarg-parsetupleandkeywords-to-pyarg-unpacktuple.md)
