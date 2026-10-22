# integers C API: `PyLong_FromString()`, `PyLong_FromUnicodeObject()`, `PyLong_FromVoidPtr()`, `PyLong_FromNativeBytes()`, `PyLong_FromUnsignedNativeBytes()`, `PyLong_FromPid()`, `PyLong_AsLong()`, `PyLong_AS_LONG()`, `PyLong_AsInt()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromString(const char *str, char **pend, int base)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Produces a fresh `PyLongObject` from the textual value held in *str*, parsed using the radix given by *base*, or `NULL` should it fail. When *pend* is non-`NULL`, **pend* is left pointing past the end of *str* on success, or at the earliest character that could not be parsed when an error occurs. A *base* of `0` causes *str* to be parsed per the [Integer literals](https://docs.python.org/3.14/reference/lexical_analysis.html#integers) definition; under that rule, a non-zero decimal number carrying leading zeros triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Where *base* is not `0`, it has to fall within `2` and `36`, inclusive. Surrounding whitespace, plus lone underscores placed after a base specifier and between digits, are skipped. A `ValueError` is raised whenever no digits appear, or whenever *str* lacks a NULL terminator after the digits and any trailing whitespace.

See also

The `PyLong_AsNativeBytes()` and `PyLong_FromNativeBytes()` functions handle conversion of a `PyLongObject` to or from a byte array expressed in base `256`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUnicodeObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *u, int base)

*Return value: New reference.*

Turns a run of Unicode digits held in the string *u* into a Python integer value.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromVoidPtr(void *p)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a Python integer out of the pointer *p*. You can recover the pointer afterward from the produced value by calling `PyLong_AsVoidPtr()`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromNativeBytes(const void *buffer, size_t n_bytes, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Builds a Python integer from whatever value sits in the leading *n_bytes* of *buffer*, read as a two's-complement signed number.

The *flags* match those of `PyLong_AsNativeBytes()`. Supplying `-1` picks the native endianness CPython was built with and treats the top bit as a sign bit. Supplying `Py_ASNATIVEBYTES_UNSIGNED_BUFFER` yields the same outcome as a call to `PyLong_FromUnsignedNativeBytes()`. Any remaining flags have no effect.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyLong_FromUnsignedNativeBytes(const void *buffer, size_t n_bytes, int flags)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

Builds a Python integer from whatever value sits in the leading *n_bytes* of *buffer*, read as an unsigned number.

The *flags* match those of `PyLong_AsNativeBytes()`. Supplying `-1` picks the native endianness CPython was built with and assumes the top bit is not a sign bit. Apart from endianness, the flags are disregarded.

Added in version 3.13.

 PyLong_FromPid(pid)

A macro that builds a Python integer out of a process identifier.

Depending on how wide the platform's PID type is, it may resolve to either `PyLong_FromLong()` or `PyLong_FromLongLong()`.

Added in version 3.2.

 long PyLong_AsLong([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yields a C long form of *obj*. When *obj* is not itself a `PyLongObject` instance, its [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method is invoked first (when one exists) to turn it into a `PyLongObject`.

A [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised when the magnitude of *obj* exceeds what a long can hold.

On error the result is `-1`. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to disambiguate.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

Changed in version 3.10: This function will no longer use [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__).

 long PyLong_AS_LONG([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Behaves precisely like the preferred `PyLong_AsLong`. As such, it too may fail with [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) or some other exception.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.14.

 int PyLong_AsInt([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Works like `PyLong_AsLong()`, except the outcome lands in a C int rather than a C long.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Following source contract](pylong-aslongandoverflow-to-pylong-assize-t.md)
