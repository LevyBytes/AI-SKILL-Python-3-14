# unicode C API: Unicode writer lifecycle and write operations

type PyUnicodeWriter

A Unicode writer instance.

Tear the instance down with `PyUnicodeWriter_Finish()` when things go well, or `PyUnicodeWriter_Discard()` when they don't.

 PyUnicodeWriter *PyUnicodeWriter_Create([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length)

Spin up a Unicode writer instance.

The *length* value cannot be below `0`.

When *length* exceeds `0`, an internal buffer sized for *length* characters is reserved ahead of time.

On failure, raise an exception and give back `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeWriter_Finish(PyUnicodeWriter *writer)

Hand back the finished Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object and dispose of the writer instance.

On failure, raise an exception and give back `NULL`.

Once this returns, the writer instance is no longer usable.

 void PyUnicodeWriter_Discard(PyUnicodeWriter *writer)

Throw away the internal Unicode buffer and dispose of the writer instance.

Where *writer* is `NULL`, nothing happens.

Once this returns, the writer instance is no longer usable.

 int PyUnicodeWriter_WriteChar(PyUnicodeWriter *writer, Py_UCS4 ch)

Place the lone Unicode character *ch* into *writer*.

A `0` comes back when this works; otherwise an exception is set, *writer* is left as it stood, and `-1` is returned.

 int PyUnicodeWriter_WriteUTF8(PyUnicodeWriter *writer, const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Take the string *str*, decode it from UTF-8 under strict mode, and feed the result into *writer*.

The byte count of the string is *size*. Where *size* equals `-1`, `strlen(str)` is invoked to obtain that length.

A `0` comes back when this works; otherwise an exception is set, *writer* is left as it stood, and `-1` is returned.

See also `PyUnicodeWriter_DecodeUTF8Stateful()`.

 int PyUnicodeWriter_WriteASCII(PyUnicodeWriter *writer, const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Put the ASCII string *str* into *writer*.

The byte count of the string is *size*. Where *size* equals `-1`, `strlen(str)` is invoked to obtain that length.

Only ASCII characters are permitted in *str*; supply non-ASCII content and the behavior becomes undefined.

When it succeeds `0` is handed back; on failure an exception gets set, *writer* stays untouched, and the call yields `-1`.

 int PyUnicodeWriter_WriteWideChar(PyUnicodeWriter *writer, const wchar_t *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Put the wide string *str* into *writer*.

Here *size* counts wide characters. Where *size* equals `-1`, `wcslen(str)` is invoked to obtain that length.

When it succeeds `0` is handed back; on failure an exception gets set, *writer* stays untouched, and the call yields `-1`.

 int PyUnicodeWriter_WriteUCS4(PyUnicodeWriter *writer, Py_UCS4 *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Put the UCS4 string *str* into *writer*.

Here *size* counts UCS4 characters.

When it succeeds `0` is handed back; on failure an exception gets set, *writer* stays untouched, and the call yields `-1`.

 int PyUnicodeWriter_WriteStr(PyUnicodeWriter *writer, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Run [`PyObject_Str()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Str) over *obj* and route what comes out into *writer*.

Returning `0` marks success; should it fail, an exception is raised, *writer* keeps its prior contents, and `-1` results.

If you're emitting a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) subclass that overrides [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__), reach for `PyUnicode_FromObject()` to recover the underlying string.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicodewriter.md) · [Following source contract](unicode-writer-repr-and-utf8-decoding.md)
