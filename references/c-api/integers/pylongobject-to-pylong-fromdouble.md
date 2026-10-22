# integers C API: Integer types and construction from C numeric values

type PyLongObject

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) (as an opaque struct).*

A Python integer object is modeled by this subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyLong_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The Python integer type is captured by this instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject). It is identical to the object exposed as [`int`](https://docs.python.org/3.14/library/functions.html#int) at the Python level.

 int PyLong_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Returns true when the supplied argument is a `PyLongObject` or any subtype of `PyLongObject`. The call never fails.

 int PyLong_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Returns true when the supplied argument is a `PyLongObject` while excluding subtypes of `PyLongObject`. The call never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromLong(long v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from *v*, or `NULL` should it fail.

**CPython implementation detail:** Every integer from `-5` through `256` is held by CPython in a preallocated array of integer objects. Constructing an int within that span simply hands you a reference back to the already-existing object.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUnsignedLong(unsigned long v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from a C unsigned long, or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromSsize_t([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from a C [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t), or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromSize_t(size_t v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from a C `size_t`, or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromLongLong(long long v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from a C long long, or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUnsignedLongLong(unsigned long long v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from a C unsigned long long, or `NULL` should it fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromInt32(int32_t value)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromInt64(int64_t value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Produces a fresh `PyLongObject` object built from a signed C int32_t or int64_t, or `NULL` together with an exception set should it fail.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUInt32(uint32_t value)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUInt64(uint64_t value)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Produces a fresh `PyLongObject` object built from an unsigned C uint32_t or uint64_t, or `NULL` together with an exception set should it fail.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromDouble(double v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` object built from the integer part of *v*, or `NULL` should it fail.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Following source contract](pylong-fromstring-to-pylong-asint.md)
