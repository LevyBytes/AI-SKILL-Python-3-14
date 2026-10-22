# What's new in Python 3.14 / C API changes / Deprecated C APIs / Pending removal in Python 3.18

#### Pending removal in Python 3.18

- These private helpers carry a deprecation and are slated to disappear in Python 3.18:

  - `_PyBytes_Join()`: use [`PyBytes_Join()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Join).

  - `_PyDict_GetItemStringWithError()`: use [`PyDict_GetItemStringRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemStringRef).

  - `_PyDict_Pop()`: use [`PyDict_Pop()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Pop).

  - `_PyLong_Sign()`: use [`PyLong_GetSign()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetSign).

  - `_PyLong_FromDigits()` and `_PyLong_New()`: use [`PyLongWriter_Create()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Create).

  - `_PyThreadState_UncheckedGet()`: use [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked).

  - `_PyUnicode_AsString()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8).

  - `_PyUnicodeWriter_Init()`: replace `_PyUnicodeWriter_Init(&writer)` with [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create).

  - `_PyUnicodeWriter_Finish()`: replace `_PyUnicodeWriter_Finish(&writer)` with [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish).

  - `_PyUnicodeWriter_Dealloc()`: replace `_PyUnicodeWriter_Dealloc(&writer)` with [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard).

  - `_PyUnicodeWriter_WriteChar()`: replace `_PyUnicodeWriter_WriteChar(&writer, ch)` with [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar).

  - `_PyUnicodeWriter_WriteStr()`: replace `_PyUnicodeWriter_WriteStr(&writer, str)` with [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr).

  - `_PyUnicodeWriter_WriteSubstring()`: replace `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` with [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring).

  - `_PyUnicodeWriter_WriteASCIIString()`: replace `_PyUnicodeWriter_WriteASCIIString(&writer, str)` with [`PyUnicodeWriter_WriteASCII(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII).

  - `_PyUnicodeWriter_WriteLatin1String()`: replace `_PyUnicodeWriter_WriteLatin1String(&writer, str)` with [`PyUnicodeWriter_WriteUTF8(writer, str)`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8).

  - `_PyUnicodeWriter_Prepare()`: (no replacement).

  - `_PyUnicodeWriter_PrepareKind()`: (no replacement).

  - `_Py_HashPointer()`: use [`Py_HashPointer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashPointer).

  - `_Py_fopen_obj()`: use [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen).

To obtain these freshly public functions on Python 3.13 and earlier, the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/) is available. (Contributed by Victor Stinner in [gh-128863](https://github.com/python/cpython/issues/128863).)

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-16.md) · [Next source section](c-api-unscheduled-removals.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md)
