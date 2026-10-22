# integers C API: `PyLong_AsUnsignedLongLong()`, `PyLong_AsUnsignedLongMask()`, `PyLong_AsUnsignedLongLongMask()`, `PyLong_AsInt32()`, `PyLong_AsInt64()`, `PyLong_AsUInt32()`, `PyLong_AsUInt64()`

unsigned long long PyLong_AsUnsignedLongLong([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *pylong)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C unsigned long long form of *pylong*. Here *pylong* has to be a `PyLongObject` instance.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *pylong* exceeds what an unsigned long long can hold.

On error the result is `(unsigned long long)-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.1: A negative *pylong* now raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError), not [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 unsigned long PyLong_AsUnsignedLongMask([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C unsigned long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

When the magnitude of *obj* lies beyond what an unsigned long covers, the value reduced modulo `ULONG_MAX + 1` is returned.

On error the result is `(unsigned long)-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 unsigned long long PyLong_AsUnsignedLongLongMask([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C unsigned long long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

When the magnitude of *obj* lies beyond what an unsigned long long covers, the value reduced modulo `ULLONG_MAX + 1` is returned.

On error the result is `(unsigned long long)-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 int PyLong_AsInt32([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int32_t *value)

 int PyLong_AsInt64([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int64_t *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Stores into **value* a signed C int32_t or int64_t form of *obj*.

When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

Should the *obj* value lie outside the valid span, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

On success **value* is written and `0` returned. On error an exception is set and `-1` returned.

*value* must not be `NULL`.

Added in version 3.14.

 int PyLong_AsUInt32([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, uint32_t *value)

 int PyLong_AsUInt64([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, uint64_t *value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Stores into **value* an unsigned C uint32_t or uint64_t form of *obj*.

When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

- Should *obj* be negative, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

- Should the *obj* value lie outside the valid span, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

On success **value* is written and `0` returned. On error an exception is set and `-1` returned.

*value* must not be `NULL`.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Previous source contract](pylong-aslongandoverflow-to-pylong-assize-t.md) · [Following source contract](pylong-asdouble-to-pylong-asvoidptr.md)
