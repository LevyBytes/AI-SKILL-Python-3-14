# Direct API functions

### Direct API functions

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyByteArray_FromObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Build and hand back a fresh bytearray sourced from *o*, provided *o* supports the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

When this does not succeed, `NULL` comes back and an exception has been set.

Note

For an object exposing the buffer interface, do not alter that buffer for as long as the bytearray is being assembled.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyByteArray_FromStringAndSize(const char *string, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Construct a brand-new bytearray out of *string* together with the length *len*.

Should this fail, the result is `NULL` and an exception is set.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyByteArray_Concat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *a, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *b)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Join the two bytearrays *a* and *b*, handing back a freshly built bytearray that holds the combined data.

If it does not work, the call yields `NULL` after setting an exception.

Note

When the source object provides the buffer protocol, its buffer has to stay unchanged for the duration of building the bytearray.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyByteArray_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytearray)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Once a `NULL` pointer check has passed, give back the size of *bytearray*.

 char *PyByteArray_AsString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytearray)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

After a `NULL` pointer check, hand back what *bytearray* holds as a char array; one extra null byte is always tacked on to that array.

Note

Modifying the bytearray from another thread while the returned char array is still in use is not safe.

 int PyByteArray_Resize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytearray, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Grow or shrink the buffer that *bytearray* holds internally so it spans *len*. A `-1` result, paired with a set exception, signals failure.

Changed in version 3.14: Supplying a negative *len* now raises by setting an exception and giving back -1.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pybytearrayobject-to-pybytearray-type.md) · [Previous source contract](pybytearray-check-to-pybytearray-checkexact.md) · [Following source contract](pybytearray-as-string-to-pybytearray-get-size.md)
