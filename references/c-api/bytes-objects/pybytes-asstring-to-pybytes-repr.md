# bytes objects C API: `PyBytes_AsString()`, `PyBytes_AS_STRING()`, `PyBytes_AsStringAndSize()`, `PyBytes_Concat()`, `PyBytes_ConcatAndDel()`, `PyBytes_Join()`, `_PyBytes_Resize()`, `PyBytes_Repr()`

char *PyBytes_AsString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Hand back a pointer aimed at the contents of *o*. That pointer points into the internal buffer of *o*, spanning `len(o) + 1` bytes. Whatever other null bytes exist, the final byte in this buffer is always null. Do not change the data at all and do not free it, with the sole exception of an object freshly made via `PyBytes_FromStringAndSize(NULL, size)`. Where *o* turns out not to be a bytes value, `PyBytes_AsString()` yields `NULL` and raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 char *PyBytes_AS_STRING([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *string)

* Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Resembles `PyBytes_AsString()`, with the error checking left out.

 int PyBytes_AsStringAndSize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, char **buffer, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *length)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-compatible).*

Deliver the null-terminated contents of *obj* via the out-parameters *buffer* and *length*. A `0` result means success.

Should *length* be `NULL`, embedded null bytes are forbidden in the bytes value; if any are present, the call hands back `-1` and a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

What *buffer* points at is *obj*'s own internal storage, carrying one more null byte at the tail that *length* leaves out. Leave the data unmodified and never free it, unless the object was just built with `PyBytes_FromStringAndSize(NULL, size)`. When *obj* is not actually a bytes value, `PyBytes_AsStringAndSize()` gives back `-1` and raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.5: In earlier releases, hitting embedded null bytes inside the bytes value triggered [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 void PyBytes_Concat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **bytes, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *newpart)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Produce a fresh bytes value at **bytes* that holds *newpart* tacked onto *bytes*; ownership of that new reference passes to the caller, while the reference held by the former *bytes* is stolen. Where building the new value is impossible, that old *bytes* reference is dropped anyway, **bytes* becomes `NULL`, and a fitting exception is set.

Note

When *newpart* supports the buffer protocol, keep its buffer unchanged throughout the creation of the new bytes value.

 void PyBytes_ConcatAndDel([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **bytes, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *newpart)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Build a fresh bytes value at **bytes* made of *newpart* joined to the end of *bytes*. Unlike the previous routine, this one lets go of the [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to *newpart*, dropping its reference count by one.

Note

Given that *newpart* offers the buffer protocol, its buffer must stay constant while the new bytes value is being put together.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_Join([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sep, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iterable)

* Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Comparable to writing `sep.join(iterable)` from Python.

*sep* is required to be a Python [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. (Be aware that [`PyUnicode_Join()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Join) will take a `NULL` separator and read it as a space, while `PyBytes_Join()` rejects a `NULL` separator.)

*iterable* has to be something iterable whose elements each support the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects).

When it succeeds, a fresh [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object comes back. On error, an exception is set and `NULL` is returned.

Added in version 3.14.

Note

Where the *iterable* members offer the buffer protocol, none of their buffers may change while the new bytes value is being assembled.

 int _PyBytes_Resize([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **bytes, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) newsize)

* Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-distinct).*

Change the length of a bytes value, where *newsize* becomes its new length. Picture it as forging a fresh bytes value and tearing down the previous one, just done more efficiently. Hand in the address of an existing bytes value as a writable lvalue along with the size you want. On success, **bytes* refers to the resized value and `0` comes back, though the address stored in **bytes* may not match what you passed in. Should the reallocation not work, the original value at **bytes* is freed, **bytes* is cleared to `NULL`, [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) is set, and `-1` is the result.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_Repr([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bytes, int smartquotes)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Obtain the string rendering of *bytes*. At present this routine backs Python's `bytes.__repr__()`.

No type check happens here; handing *bytes* a non-bytes value or `NULL` leads to undefined behavior.

With *smartquotes* set true, the output switches to double quotes rather than single quotes whenever *bytes* itself contains single quotes. To illustrate, the byte string `'Python'` shows up as `b"'Python'"` while *smartquotes* is true, and as `b'\'Python\''` while it is false.

When it works, you get back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) pointing to a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object that holds the representation. If it does not, the result is `NULL` together with a set exception.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](bytes-objects.md) · [Owning structure and shared ABI conditions](pybytesobject-to-pybytes-get-size.md) · [Following source contract](pybytes-decodeescape.md)
