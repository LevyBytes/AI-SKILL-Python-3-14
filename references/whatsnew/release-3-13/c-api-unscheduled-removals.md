# What's New In Python 3.13 / C API Changes / Deprecated C APIs / Pending removal in future versions

#### Pending removal in future versions

These APIs below carry a deprecation, yet no removal date has been fixed for them so far.

- [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE): Unneeded since Python 3.8.

- [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch): adopt [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) as the replacement.

- [`PyErr_NormalizeException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NormalizeException): adopt [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) as the replacement.

- [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore): adopt [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) as the replacement.

- [`PyModule_GetFilename()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetFilename): adopt [`PyModule_GetFilenameObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetFilenameObject) as the replacement.

- [`PyOS_AfterFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork): adopt [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) as the replacement.

- [`PySlice_GetIndicesEx()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_GetIndicesEx): adopt [`PySlice_Unpack()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_Unpack) together with [`PySlice_AdjustIndices()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_AdjustIndices).

- [`PyUnicode_READY()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READY): Unneeded since Python 3.12

- `PyErr_Display()`: adopt [`PyErr_DisplayException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_DisplayException) as the replacement.

- `_PyErr_ChainExceptions()`: adopt `_PyErr_ChainExceptions1()` as the replacement.

- `PyBytesObject.ob_shash` member: call [`PyObject_Hash()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Hash) instead.

- Thread Local Storage (TLS) API:

  -

[`PyThread_create_key()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_create_key): Use [`PyThread_tss_alloc()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_alloc) instead.

  - [`PyThread_delete_key()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_delete_key): Use [`PyThread_tss_free()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_free) instead.

  - [`PyThread_set_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_set_key_value): Use [`PyThread_tss_set()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_set) instead.

  - [`PyThread_get_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_get_key_value): Use [`PyThread_tss_get()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_get) instead.

  - [`PyThread_delete_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_delete_key_value): Use [`PyThread_tss_delete()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_delete) instead.

  - [`PyThread_ReInitTLS()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_ReInitTLS): Unneeded since Python 3.7.

[Subject index](INDEX.md) · [Previous source section](c-api-removals-scheduled-for-3-18.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-c-apis.md) · [Next source section](build-changes.md)
