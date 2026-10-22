# Python 3.14.0 alpha 5 / c api / bytes

[gh-128863](https://github.com/python/cpython/issues/128863): These private functions are now deprecated, with removal scheduled for Python 3.18:

  - `_PyBytes_Join()`: use [`PyBytes_Join()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Join).

  - `_PyDict_GetItemStringWithError()`: use [`PyDict_GetItemStringRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemStringRef).

  - `_PyDict_Pop()`: use [`PyDict_Pop()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Pop).

  - `_PyLong_Sign()`: use [`PyLong_GetSign()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetSign).

  - `_PyLong_FromDigits()` and `_PyLong_New()`: use [`PyLongWriter_Create()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Create).

  - `_PyThreadState_UncheckedGet()`: use [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked).

  - `_PyUnicode_AsString()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUTF8).

  - `_Py_HashPointer()`: use [`Py_HashPointer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashPointer).

  - `_Py_fopen_obj()`: use [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen).

To obtain these freshly public functions on Python 3.13 and earlier, lean on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
