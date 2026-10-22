# Python 3.13 changes: Removed buffers, call helpers and initialization APIs

### Removed C APIs

- Drop a number of functions, macros, variables, and similar items whose names carry the `_Py` or `_PY` prefix (treated as private). When one of these deletions hits your project and you feel the dropped API ought to stay available, please [open a new issue](https://docs.python.org/3.14/bugs.html#using-the-tracker) asking for a public C API, and add `cc: @vstinner` to it so Victor Stinner is notified. (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320).)

- Drop the legacy buffer protocols that Python 3.0 deprecated. Reach for the [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) in their place.

  - `PyObject_CheckReadBuffer()`: Reach for [`PyObject_CheckBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_CheckBuffer) when checking whether an object honors the buffer protocol. Bear in mind that `PyObject_CheckBuffer()` offers no assurance that [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) will go through. For confirming the object can genuinely be read, refer to the upcoming `PyObject_GetBuffer()` example.

  - `PyObject_AsCharBuffer()`, `PyObject_AsReadBuffer()`: Reach for [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) together with [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release) in their place:

```c
Py_buffer view;
if (PyObject_GetBuffer(obj, &view, PyBUF_SIMPLE) < 0) {
    return NULL;
}
// Use `view.buf` and `view.len` to read from the buffer.
// You may need to cast buf as `(const char*)view.buf`.
PyBuffer_Release(&view);

```

  - `PyObject_AsWriteBuffer()`: Reach for [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) together with [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release) in their place:

```c
Py_buffer view;
if (PyObject_GetBuffer(obj, &view, PyBUF_WRITABLE) < 0) {
    return NULL;
}
// Use `view.buf` and `view.len` to write to the buffer.
PyBuffer_Release(&view);

```

(Contributed by Inada Naoki in [gh-85275](https://github.com/python/cpython/issues/85275).)

- Drop several functions that Python 3.9 deprecated:

  - `PyEval_CallObject()`, `PyEval_CallObjectWithKeywords()`: Reach for [`PyObject_CallNoArgs()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallNoArgs) or [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) in their place.

Warning

Within [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call), the positional arguments are required to be a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) and not `NULL`, while the keyword arguments are required to be a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) or `NULL`; by contrast, the dropped functions verified argument types and tolerated `NULL` positional and keyword arguments. When trading `PyEval_CallObjectWithKeywords(func, NULL, kwargs)` for [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call), supply an empty tuple as the positional arguments by way of [`PyTuple_New(0)`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTuple_New).

  - `PyEval_CallFunction()`: Reach for [`PyObject_CallFunction()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallFunction) in its place.

  - `PyEval_CallMethod()`: Reach for [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod) in its place.

  - `PyCFunction_Call()`: Reach for [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) in its place.

(Contributed by Victor Stinner in [gh-105107](https://github.com/python/cpython/issues/105107).)

- Drop the following legacy functions for configuring Python startup, which Python 3.11 deprecated:

  - `PySys_AddWarnOptionUnicode()`: Reach for [`PyConfig.warnoptions`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.warnoptions) in its place.

  - `PySys_AddWarnOption()`: Reach for [`PyConfig.warnoptions`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.warnoptions) in its place.

- `PySys_AddXOption()`: Reach for [`PyConfig.xoptions`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.xoptions) in its place.

  - `PySys_HasWarnOptions()`: Reach for [`PyConfig.xoptions`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.xoptions) in its place.

  - `PySys_SetPath()`: Assign [`PyConfig.module_search_paths`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths) in its place.

  - `Py_SetPath()`: Assign [`PyConfig.module_search_paths`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths) in its place.

  - `Py_SetStandardStreamEncoding()`: Assign [`PyConfig.stdio_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.stdio_encoding) in its place, and perhaps also assign [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) (on Windows).

  - `_Py_SetProgramFullPath()`: Assign [`PyConfig.executable`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.executable) in its place.

Adopt the fresh [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) API from the [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config) instead ([**PEP 587**](https://peps.python.org/pep-0587/)), which arrived in Python 3.8. (Contributed by Victor Stinner in [gh-105145](https://github.com/python/cpython/issues/105145).)

- Drop the `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` functions, which Python 3.2 deprecated. The current thread state went unchanged by them. Suitable substitutes include:

  - [`PyEval_SaveThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_SaveThread) and [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread);

  - low-level [`PyEval_AcquireThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_AcquireThread) and [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread);

  - or [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) and [`PyGILState_Release()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Release).

(Contributed by Victor Stinner in [gh-105182](https://github.com/python/cpython/issues/105182).)

-

[Subject index](INDEX.md) · [Previous source section](c-api-changes-limited-c-api-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Following release/subject continuation](removed-thread-and-internal-apis.md)
