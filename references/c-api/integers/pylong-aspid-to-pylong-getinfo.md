# integers C API: `PyLong_AsPid()`, `PyLong_GetSign()`, `PyLong_IsPositive()`, `PyLong_IsNegative()`, `PyLong_IsZero()`, `PyLong_GetInfo()`

At present, a value of `-1` maps to `Py_ASNATIVEBYTES_NATIVE_ENDIAN | Py_ASNATIVEBYTES_UNSIGNED_BUFFER`.

| Flag | Value |
| --- | --- |
| Py_ASNATIVEBYTES_DEFAULTS * Part of the Stable ABI since version 3.14.* | `-1` |
| Py_ASNATIVEBYTES_BIG_ENDIAN * Part of the Stable ABI since version 3.14.* | `0` |
| Py_ASNATIVEBYTES_LITTLE_ENDIAN * Part of the Stable ABI since version 3.14.* | `1` |
| Py_ASNATIVEBYTES_NATIVE_ENDIAN * Part of the Stable ABI since version 3.14.* | `3` |
| Py_ASNATIVEBYTES_UNSIGNED_BUFFER * Part of the Stable ABI since version 3.14.* | `4` |
| Py_ASNATIVEBYTES_REJECT_NEGATIVE * Part of the Stable ABI since version 3.14.* | `8` |
| Py_ASNATIVEBYTES_ALLOW_INDEX * Part of the Stable ABI since version 3.14.* | `16` |

When you give `Py_ASNATIVEBYTES_NATIVE_ENDIAN`, it takes precedence over every other endian flag. The value `2`, meanwhile, is held in reserve.

Out of the box, the buffer requested is large enough to make room for a sign bit. To illustrate, converting 128 while *n_bytes=1* leads the function to give back 2 (or more) so that a zero sign bit can be stored.

Should you supply `Py_ASNATIVEBYTES_UNSIGNED_BUFFER`, the size calculations leave out a zero sign bit. That, for instance, lets 128 squeeze into a single-byte buffer. Were the destination buffer afterward read as signed, a positive input could turn negative. Keep in mind that this flag leaves the treatment of negative values untouched: with those, room for a sign bit is requested every time.

Handing in `Py_ASNATIVEBYTES_REJECT_NEGATIVE` makes an exception get set whenever *pylong* is negative. Leave that flag off and negative values are copied as long as room exists for one or more sign bits, no matter whether `Py_ASNATIVEBYTES_UNSIGNED_BUFFER` was given.

Where `Py_ASNATIVEBYTES_ALLOW_INDEX` is given and the value passed is not an integer, that value's [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method runs first. Doing so can execute Python code and let other threads proceed, which might alter other objects or values currently in play. With *flags* set to `-1`, this option stays off, and a non-integer value raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Note

Under the default *flags* (`-1`, that is *UNSIGNED_BUFFER* lacking *REJECT_NEGATIVE*), several Python integers may land on one value with no overflow. By way of illustration, `255` and `-1` alike fit a single-byte buffer and turn on every one of its bits. Such conduct lines up with the usual C cast behavior.

Added in version 3.13.

 PyLong_AsPid(pid)

A macro that turns a Python integer into a process identifier.

It may be set up as an alias for `PyLong_AsLong()`, `PyLong_FromLongLong()`, or `PyLong_AsInt()`, the choice hinging on how large the system's PID type is.

Added in version 3.2.

 int PyLong_GetSign([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, int *sign)

Retrieve the sign carried by the integer object *obj*.

When it succeeds, write the integer sign into `*sign` (with 0, -1 or +1 standing for a zero, negative or positive integer in turn) and hand back 0.

When it fails, hand back -1 and leave an exception set. This function never fails as long as *obj* is a `PyLongObject` or one of its subtypes.

Added in version 3.14.

 int PyLong_IsPositive([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Test whether the integer object *obj* comes out positive (`obj > 0`).

Provided *obj* is an instance of `PyLongObject` or one of its subtypes, give back `1` if it is positive and `0` if not. Failing that, set an exception and give back `-1`.

Added in version 3.14.

 int PyLong_IsNegative([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Test whether the integer object *obj* comes out negative (`obj < 0`).

As long as *obj* is an instance of `PyLongObject` or a subtype thereof, return `1` should it be negative and `0` if it is not. Otherwise, set an exception and return `-1`.

Added in version 3.14.

 int PyLong_IsZero([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Test whether the integer object *obj* equals zero.

When *obj* is an instance of `PyLongObject` or a subtype of it, return `1` if it is zero and `0` if it is not. In any other case, set an exception and return `-1`.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_GetInfo(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Upon success, hand back a read only [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying details about how Python represents integers internally. Turn to [`sys.int_info`](https://docs.python.org/3.14/library/sys.html#sys.int_info) for an account of the separate fields.

Upon failure, hand back `NULL` and leave an exception set.

Added in version 3.1.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [API declaration, ownership, ABI and error contract](pylong-asnativebytes.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Following source contract](pyunstable-long-iscompact-to-pyunstable-long-compactvalue.md)
