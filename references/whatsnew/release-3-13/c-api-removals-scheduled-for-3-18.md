# What's New In Python 3.13 / C API Changes / Deprecated C APIs / Pending removal in Python 3.18

#### Pending removal in Python 3.18

- These private functions below carry a deprecation and are slated for removal in Python 3.18:

  - `_PyBytes_Join()`: switch to [`PyBytes_Join()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Join).

  - `_PyDict_GetItemStringWithError()`: switch to [`PyDict_GetItemStringRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemStringRef).

  - `_PyDict_Pop()`: switch to [`PyDict_Pop()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Pop).

  - `_PyLong_Sign()`: switch to [`PyLong_GetSign()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetSign).

  - `_PyLong_FromDigits()` and `_PyLong_New()`: switch to [`PyLongWriter_Create()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Create).

  - `_PyThreadState_UncheckedGet()`: switch to [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked).

  - `_PyUnicode_AsString()`: switch to [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8).

  - `_PyUnicodeWriter_Init()`: swap `_PyUnicodeWriter_Init(&writer)` for [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create).

  - `_PyUnicodeWriter_Finish()`: swap `_PyUnicodeWriter_Finish(&writer)` for [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish).

  - `_PyUnicodeWriter_Dealloc()`: swap `_PyUnicodeWriter_Dealloc(&writer)` for [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard).

  - `_PyUnicodeWriter_WriteChar()`: swap `_PyUnicodeWriter_WriteChar(&writer, ch)` for [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar).

  - `_PyUnicodeWriter_WriteStr()`: swap `_PyUnicodeWriter_WriteStr(&writer, str)` for [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr).

  - `_PyUnicodeWriter_WriteSubstring()`: swap `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` for [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring).

  - `_PyUnicodeWriter_WriteASCIIString()`: swap `_PyUnicodeWriter_WriteASCIIString(&writer, str)` for [`PyUnicodeWriter_WriteASCII(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII).

  - `_PyUnicodeWriter_WriteLatin1String()`: swap `_PyUnicodeWriter_WriteLatin1String(&writer, str)` for [`PyUnicodeWriter_WriteUTF8(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8).

  - `_PyUnicodeWriter_Prepare()`: (no replacement).

  - `_PyUnicodeWriter_PrepareKind()`: (no replacement).

  - `_Py_HashPointer()`: switch to [`Py_HashPointer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashPointer).

  - `_Py_fopen_obj()`: switch to [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen).

To obtain these new public functions on Python 3.13 and earlier, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/). (Contributed by Victor Stinner in [gh-128863](https://github.com/python/cpython/issues/128863).)

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-16.md) · [Next source section](c-api-unscheduled-removals.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md)
