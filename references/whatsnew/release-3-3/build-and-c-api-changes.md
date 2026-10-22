# What's New In Python 3.3 / Build and C API Changes

### Build and C API Changes

The build process for Python and the C API saw these changes:

- A new function tied to [**PEP 3118**](https://peps.python.org/pep-3118/):

  - [`PyMemoryView_FromMemory()`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyMemoryView_FromMemory)

- Fresh Unicode types, macros, and functions arrived with [**PEP 393**](https://peps.python.org/pep-0393/):

  - High-level API:

    - [`PyUnicode_CopyCharacters()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CopyCharacters)

    - [`PyUnicode_FindChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FindChar)

    - [`PyUnicode_GetLength()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GetLength), [`PyUnicode_GET_LENGTH`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GET_LENGTH)

    - [`PyUnicode_New()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_New)

    - [`PyUnicode_Substring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Substring)

    - [`PyUnicode_ReadChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_ReadChar), [`PyUnicode_WriteChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_WriteChar)

  - Low-level API:

    - [`Py_UCS1`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS1), [`Py_UCS2`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS2), [`Py_UCS4`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UCS4) types

    - [`PyASCIIObject`](https://docs.python.org/3.14/c-api/unicode.html#c.PyASCIIObject) and [`PyCompactUnicodeObject`](https://docs.python.org/3.14/c-api/unicode.html#c.PyCompactUnicodeObject) structures

    - [`PyUnicode_READY`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READY)

    - [`PyUnicode_FromKindAndData()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromKindAndData)

    - [`PyUnicode_AsUCS4()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUCS4), [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUCS4Copy)

    - [`PyUnicode_DATA`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DATA), [`PyUnicode_1BYTE_DATA`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_1BYTE_DATA), [`PyUnicode_2BYTE_DATA`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_2BYTE_DATA), [`PyUnicode_4BYTE_DATA`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_4BYTE_DATA)

    - [`PyUnicode_KIND`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_KIND) with `PyUnicode_Kind` enum: `PyUnicode_WCHAR_KIND`, [`PyUnicode_1BYTE_KIND`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_1BYTE_KIND), [`PyUnicode_2BYTE_KIND`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_2BYTE_KIND), [`PyUnicode_4BYTE_KIND`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_4BYTE_KIND)

    - [`PyUnicode_READ`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READ), [`PyUnicode_READ_CHAR`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READ_CHAR), [`PyUnicode_WRITE`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_WRITE)

    - [`PyUnicode_MAX_CHAR_VALUE`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_MAX_CHAR_VALUE)

- For the `c` format, [`PyArg_ParseTuple`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) henceforth accepts a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) ([bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380)).

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](unsupported-operating-systems.md)
