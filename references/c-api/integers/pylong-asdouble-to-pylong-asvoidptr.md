# integers C API: `PyLong_AsDouble()`, `PyLong_AsVoidPtr()`

double PyLong_AsDouble([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C double form of *pylong*. Here *pylong* has to be a `PyLongObject` instance.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *pylong* exceeds what a double can hold.

On error the result is `-1.0`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

 void *PyLong_AsVoidPtr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Turns the Python integer *pylong* into a C void pointer. Where *pylong* resists conversion, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) gets raised. A usable void pointer is guaranteed only for values that were originally made with `PyLong_FromVoidPtr()`.

On error the result is `NULL`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Previous source contract](pylong-asunsignedlonglong-to-pylong-asuint64.md) · [Following source contract](pylong-asnativebytes.md)
