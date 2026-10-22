# What's New In Python 3.3 / Deprecated functions and types of the C API

### Deprecated functions and types of the C API

[**PEP 393**](https://peps.python.org/pep-0393/) has deprecated [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE), which Python 4 will drop. Every function relying on this type is deprecated:

Unicode functions and methods built on [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) and [Py_UNICODE](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE)* types:

- `PyUnicode_FromUnicode`: use [`PyUnicode_FromWideChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromWideChar) or [`PyUnicode_FromKindAndData()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromKindAndData)

- `PyUnicode_AS_UNICODE`, `PyUnicode_AsUnicode()`, `PyUnicode_AsUnicodeAndSize()`: use [`PyUnicode_AsWideCharString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideCharString)

- `PyUnicode_AS_DATA`: use [`PyUnicode_DATA`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DATA) with [`PyUnicode_READ`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READ) and [`PyUnicode_WRITE`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_WRITE)

- `PyUnicode_GET_SIZE`, `PyUnicode_GetSize()`: use [`PyUnicode_GET_LENGTH`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GET_LENGTH) or [`PyUnicode_GetLength()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GetLength)

- `PyUnicode_GET_DATA_SIZE`: use `PyUnicode_GET_LENGTH(str) * PyUnicode_KIND(str)` (only work on ready strings)

- `PyUnicode_AsUnicodeCopy()`: use [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUCS4Copy) or [`PyUnicode_AsWideCharString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideCharString)

- `PyUnicode_GetMax()`

Functions and macros manipulating Py_UNICODE* strings:

- `Py_UNICODE_strlen()`: use [`PyUnicode_GetLength()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GetLength) or [`PyUnicode_GET_LENGTH`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GET_LENGTH)

- `Py_UNICODE_strcat()`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CopyCharacters) or [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat)

-

`Py_UNICODE_strcpy()`, `Py_UNICODE_strncpy()`, `Py_UNICODE_COPY()`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CopyCharacters) or [`PyUnicode_Substring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Substring)

- `Py_UNICODE_strcmp()`: use [`PyUnicode_Compare()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Compare)

- `Py_UNICODE_strncmp()`: use [`PyUnicode_Tailmatch()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Tailmatch)

- `Py_UNICODE_strchr()`, `Py_UNICODE_strrchr()`: use [`PyUnicode_FindChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FindChar)

- `Py_UNICODE_FILL()`: use [`PyUnicode_Fill()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Fill)

- `Py_UNICODE_MATCH`

Encoders:

- `PyUnicode_Encode()`: use `PyUnicode_AsEncodedObject()`

- `PyUnicode_EncodeUTF7()`

- `PyUnicode_EncodeUTF8()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8) or [`PyUnicode_AsUTF8String()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8String)

- `PyUnicode_EncodeUTF32()`

- `PyUnicode_EncodeUTF16()`

- `PyUnicode_EncodeUnicodeEscape()` use [`PyUnicode_AsUnicodeEscapeString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUnicodeEscapeString)

- `PyUnicode_EncodeRawUnicodeEscape()` use [`PyUnicode_AsRawUnicodeEscapeString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsRawUnicodeEscapeString)

- `PyUnicode_EncodeLatin1()`: use [`PyUnicode_AsLatin1String()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsLatin1String)

- `PyUnicode_EncodeASCII()`: use [`PyUnicode_AsASCIIString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsASCIIString)

- `PyUnicode_EncodeCharmap()`

- `PyUnicode_TranslateCharmap()`

- `PyUnicode_EncodeMBCS()`: use [`PyUnicode_AsMBCSString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsMBCSString) or [`PyUnicode_EncodeCodePage()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeCodePage) (with `CP_ACP` code_page)

- `PyUnicode_EncodeDecimal()`, `PyUnicode_TransformDecimalToASCII()`

[Subject index](INDEX.md) · [Previous source section](deprecated-python-modules-functions-and-methods.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](deprecated-features.md)
