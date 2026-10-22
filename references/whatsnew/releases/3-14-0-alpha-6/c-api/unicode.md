# Python 3.14.0 alpha 6 / c api / unicode

[gh-128863](https://github.com/python/cpython/issues/128863): These private functions are now deprecated and slated for removal in Python 3.18:

  - `_PyUnicodeWriter_Init()`: replace `_PyUnicodeWriter_Init(&writer)` with [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create).

  - `_PyUnicodeWriter_Finish()`: replace `_PyUnicodeWriter_Finish(&writer)` with [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish).

  - `_PyUnicodeWriter_Dealloc()`: replace `_PyUnicodeWriter_Dealloc(&writer)` with [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard).

  - `_PyUnicodeWriter_WriteChar()`: replace `_PyUnicodeWriter_WriteChar(&writer, ch)` with [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar).

  - `_PyUnicodeWriter_WriteStr()`: replace `_PyUnicodeWriter_WriteStr(&writer, str)` with [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr).

  - `_PyUnicodeWriter_WriteSubstring()`: replace `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` with [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring).

  - `_PyUnicodeWriter_WriteASCIIString()`: replace `_PyUnicodeWriter_WriteASCIIString(&writer, str)` with [`PyUnicodeWriter_WriteUTF8(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8).

  - `_PyUnicodeWriter_WriteLatin1String()`: replace `_PyUnicodeWriter_WriteLatin1String(&writer, str)` with [`PyUnicodeWriter_WriteUTF8(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8).

  - `_PyUnicodeWriter_Prepare()`: (no replacement).

  - `_PyUnicodeWriter_PrepareKind()`: (no replacement).

To obtain the new public functions on Python 3.13 as well as earlier releases, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

Patch by Victor Stinner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
