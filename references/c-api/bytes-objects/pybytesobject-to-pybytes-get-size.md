# bytes objects C API: Bytes types, creation, formatting and size access

type PyBytesObject

A Python bytes value is captured in C through this subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyBytes_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) stands for the bytes type in C, and from Python it is the very same object as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

 int PyBytes_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Reports true when *o* is a bytes value or comes from a class derived from the bytes type; this routine cannot fail.

 int PyBytes_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Reports true strictly when *o* is a bytes value and not an instance of any bytes subclass; the routine never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_FromString(const char *v)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

When it works, produce a fresh bytes value holding a duplicate of the string *v*; otherwise the result is `NULL`. You must pass a non-`NULL` *v*, since it goes unchecked.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_FromStringAndSize(const char *v, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

On success, yield a new bytes value carrying a duplicate of the string *v* with length *len*; on failure the answer is `NULL`. Should *v* be `NULL`, the bytes value is left with uninitialized contents.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_FromFormat(const char *format, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Given a C `printf()`-style *format* string plus a varying count of arguments, work out how large the resulting Python bytes value needs to be and hand back a bytes value with those values formatted in. Each supplied argument has to be a C type that lines up precisely with the format characters inside the *format* string. These format characters are supported:

| Format Characters | Type | Comment |
| --- | --- | --- |
| `%%` | *n/a* | The literal % character. |
| `%c` | int | One byte, given as a C int. |
| `%d` | int | Equivalent to `printf("%d")`. [1] |
| `%u` | unsigned int | Equivalent to `printf("%u")`. [1] |
| `%ld` | long | Equivalent to `printf("%ld")`. [1] |
| `%lu` | unsigned long | Equivalent to `printf("%lu")`. [1] |
| `%zd` | `Py_ssize_t` | Equivalent to `printf("%zd")`. [1] |
| `%zu` | size_t | Equivalent to `printf("%zu")`. [1] |
| `%i` | int | Equivalent to `printf("%i")`. [1] |
| `%x` | int | Equivalent to `printf("%x")`. [1] |
| `%s` | const char* | A C character array ending in a null. |
| `%p` | const void* | A C pointer rendered in hexadecimal. This is largely the same as `printf("%p")`, with the difference that the output always begins with the `0x` prefix no matter what the local `printf` produces. |

If a format character is not recognized, everything left in the format string is copied verbatim into the result, while any leftover arguments are thrown away.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_FromFormatV(const char *format, va_list vargs)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Works the same way as `PyBytes_FromFormat()`, only it accepts precisely two arguments.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_FromObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-shared).*

Give back the bytes form of *o*, where *o* is an object exposing the buffer protocol.

Note

For an object that offers the buffer protocol, refrain from altering its buffer for the whole time the bytes value is under construction.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyBytes_Size([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Give back how many bytes the bytes value *o* contains.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyBytes_GET_SIZE([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Acts like `PyBytes_Size()`, but skips the error checking.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](bytes-objects.md) · [Following source contract](pybytes-asstring-to-pybytes-repr.md)
