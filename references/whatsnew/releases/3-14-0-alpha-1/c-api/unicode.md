# Python 3.14.0 alpha 1 / c api / unicode

[gh-119182](https://github.com/python/cpython/issues/119182): Introduce a fresh [`PyUnicodeWriter`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter) API for building a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object:

  - [`PyUnicodeWriter_Create()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create).

  - [`PyUnicodeWriter_Discard()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard).

  - [`PyUnicodeWriter_Finish()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish).

  - [`PyUnicodeWriter_WriteChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar).

  - [`PyUnicodeWriter_WriteUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8).

  - [`PyUnicodeWriter_WriteUCS4()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUCS4).

  - [`PyUnicodeWriter_WriteWideChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteWideChar).

  - [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr).

  - [`PyUnicodeWriter_WriteRepr()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteRepr).

  - [`PyUnicodeWriter_WriteSubstring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring).

  - [`PyUnicodeWriter_Format()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Format).

  - [`PyUnicodeWriter_DecodeUTF8Stateful()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_DecodeUTF8Stateful).

Victor Stinner wrote the patch.

[gh-70278](https://github.com/python/cpython/issues/70278): [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) stops emitting the trailing `\ufffd` character for a truncated C string when precision is paired with `%s` and `%V`. The truncation now lands ahead of where truncated multibyte sequences begin.

[gh-124502](https://github.com/python/cpython/issues/124502): Bring [`PyUnicode_Equal()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Equal) into the limited C API, which checks whether two strings match. Victor Stinner wrote the patch.

[gh-113993](https://github.com/python/cpython/issues/113993): [`PyUnicode_InternInPlace()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternInPlace) stops keeping its argument safe from garbage collection.

A handful of functions accepting `char *` are now documented as potentially keeping string objects out of garbage collection; see each one's docs for the details: [`PyUnicode_InternFromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternFromString), [`PyDict_SetItemString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetItemString), [`PyObject_SetAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttrString), [`PyObject_DelAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_DelAttrString), `PyUnicode_InternFromString()`, plus the `PyModule_Add*` convenience functions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
