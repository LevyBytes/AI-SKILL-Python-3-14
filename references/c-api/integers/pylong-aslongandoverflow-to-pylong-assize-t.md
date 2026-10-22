# integers C API: `PyLong_AsLongAndOverflow()`, `PyLong_AsLongLong()`, `PyLong_AsLongLongAndOverflow()`, `PyLong_AsSsize_t()`, `PyLong_AsUnsignedLong()`, `PyLong_AsSize_t()`

long PyLong_AsLongAndOverflow([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int *overflow)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

Should the magnitude of *obj* exceed `LONG_MAX` or fall below `LONG_MIN`, **overflow* is set to `1` or `-1` accordingly and `-1` is returned; otherwise **overflow* becomes `0`. Should some unrelated exception arise, **overflow* is set to `0` and `-1` is returned in the usual way.

On error the result is `-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 long long PyLong_AsLongLong([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C long long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *obj* exceeds what a long long can hold.

On error the result is `-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 long long PyLong_AsLongLongAndOverflow([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int *overflow)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C long long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

Should the magnitude of *obj* exceed `LLONG_MAX` or fall below `LLONG_MIN`, **overflow* is set to `1` or `-1` accordingly and `-1` is returned; otherwise **overflow* becomes `0`. Should some unrelated exception arise, **overflow* is set to `0` and `-1` is returned in the usual way.

On error the result is `-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Added in version 3.2.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyLong_AsSsize_t([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) form of *pylong*. Here *pylong* has to be a `PyLongObject` instance.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *pylong* exceeds what a [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) can hold.

On error the result is `-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

 unsigned long PyLong_AsUnsignedLong([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C unsigned long form of *pylong*. Here *pylong* has to be a `PyLongObject` instance.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *pylong* exceeds what a unsigned long can hold.

On error the result is `(unsigned long)-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

 size_t PyLong_AsSize_t([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C `size_t` form of *pylong*. Here *pylong* has to be a `PyLongObject` instance.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *pylong* exceeds what a `size_t` can hold.

On error the result is `(size_t)-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Previous source contract](pylong-fromstring-to-pylong-asint.md) · [Following source contract](pylong-asunsignedlonglong-to-pylong-asuint64.md)
