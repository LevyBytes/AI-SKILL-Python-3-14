# C API pending removal in future versions: Py_TPFLAGS_HAVE_FINALIZE; PyErr_Fetch(); PyErr_NormalizeException(); PyErr_Restore(); PyModule_GetFilename(); PyOS_AfterFork(); PySlice_GetIndicesEx(); PyUnicode_READY(); PyErr_Display(); _PyErr_ChainExceptions(); PyBytesObject.ob_shash member; Thread Local Storage API

## Pending removal in future versions

### Pending removal in future versions

Although no removal date has yet been fixed, the APIs listed here are deprecated and slated to go away.

- [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE): Unneeded since Python 3.8.

- [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch): reach for [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) in its place.

- [`PyErr_NormalizeException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NormalizeException): reach for [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) in its place.

- [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore): reach for [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) in its place.

- [`PyModule_GetFilename()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetFilename): reach for [`PyModule_GetFilenameObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetFilenameObject) in its place.

- [`PyOS_AfterFork()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork): reach for [`PyOS_AfterFork_Child()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_AfterFork_Child) in its place.

- [`PySlice_GetIndicesEx()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_GetIndicesEx): reach for [`PySlice_Unpack()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_Unpack) and [`PySlice_AdjustIndices()`](https://docs.python.org/3.14/c-api/slice.html#c.PySlice_AdjustIndices) in its place.

- [`PyUnicode_READY()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_READY): Unneeded since Python 3.12

- `PyErr_Display()`: reach for [`PyErr_DisplayException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_DisplayException) in its place.

- `_PyErr_ChainExceptions()`: reach for `_PyErr_ChainExceptions1()` in its place.

- `PyBytesObject.ob_shash` member: call [`PyObject_Hash()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Hash) instead.

- Thread Local Storage (TLS) API:

  - [`PyThread_create_key()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_create_key): reach for [`PyThread_tss_alloc()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_alloc) in its place.

  - [`PyThread_delete_key()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_delete_key): reach for [`PyThread_tss_free()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_free) in its place.

  - [`PyThread_set_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_set_key_value): reach for [`PyThread_tss_set()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_set) in its place.

  - [`PyThread_get_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_get_key_value): reach for [`PyThread_tss_get()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_get) in its place.

  - [`PyThread_delete_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_delete_key_value): reach for [`PyThread_tss_delete()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_tss_delete) in its place.

  - [`PyThread_ReInitTLS()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_ReInitTLS): Unneeded since Python 3.7.

[Subject index](INDEX.md) · [Previous source section](../python-3-18/private-functions-and-replacement-apis.md)
