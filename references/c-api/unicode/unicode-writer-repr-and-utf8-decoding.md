# unicode C API: `PyUnicodeWriter_WriteRepr()`, `PyUnicodeWriter_WriteSubstring()`, `PyUnicodeWriter_Format()`, `PyUnicodeWriter_DecodeUTF8Stateful()`

int PyUnicodeWriter_WriteRepr(PyUnicodeWriter *writer, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Run [`PyObject_Repr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Repr) over *obj* and route what comes out into *writer*.

Where *obj* is `NULL`, the string `"<NULL>"` gets written into *writer* instead.

Returning `0` marks success; should it fail, an exception is raised, *writer* keeps its prior contents, and `-1` results.

Changed in version 3.14.4: Added support for `NULL`.

 int PyUnicodeWriter_WriteSubstring(PyUnicodeWriter *writer, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

Put the substring `str[start:end]` into *writer*.

A Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object is required for *str*. The *start* value has to be greater than or equal to 0, and no larger than *end*, while *end* itself must not run past the length of *str*.

Success yields `0`; on a failure an exception is raised, *writer* holds its earlier state, and `-1` is what you get back.

 int PyUnicodeWriter_Format(PyUnicodeWriter *writer, const char *format, ...)

Mirrors `PyUnicode_FromFormat()`, except the output lands straight inside *writer*.

Success yields `0`; on a failure an exception is raised, *writer* holds its earlier state, and `-1` is what you get back.

 int PyUnicodeWriter_DecodeUTF8Stateful(PyUnicodeWriter *writer, const char *string, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

Decode *str* out of UTF-8 under the *errors* error handler and route the result into *writer*.

The byte count of the string is *size*. Where *size* equals `-1`, `strlen(str)` is invoked to obtain that length.

For *errors* you give the name of an [error handler](https://docs.python.org/3.14/library/codecs.html#error-handlers), `"replace"` being one example. Leave *errors* as `NULL` and the strict handler applies.

When *consumed* isn't `NULL`, *consumed is populated on success with the tally of decoded bytes. With *consumed* set to `NULL`, any trailing partial UTF-8 byte sequence counts as an error.

A `0` returns when this works; otherwise an exception is set, *writer* is left as it stood, and `-1` is returned.

See also `PyUnicodeWriter_WriteUTF8()`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicodewriter.md) · [Owning structure and shared ABI conditions](pyunicodewriter-to-pyunicodewriter-writestr.md) · [Following source contract](deprecated-api.md)
