# What's New In Python 3.11 / C API Changes / New Features

### C API Changes

### New Features

- Introduced a fresh [`PyType_GetName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetName) function that returns the short name of a type. (Contributed by Hai Shi in [bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035).)

- Introduced a fresh [`PyType_GetQualName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetQualName) function that returns the qualified name of a type. (Contributed by Hai Shi in [bpo-42035](https://bugs.python.org/issue?@action=redirect&bpo=42035).)

- Add new [`PyThreadState_EnterTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_EnterTracing) and [`PyThreadState_LeaveTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_LeaveTracing) functions into the limited C API for pausing and resuming both tracing and profiling. (Contributed by Victor Stinner in [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760).)

- Introduced the [`Py_Version`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_Version) constant, which holds the very same value as [`PY_VERSION_HEX`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.PY_VERSION_HEX). (Contributed by Gabriele N. Tornetta in [bpo-43931](https://bugs.python.org/issue?@action=redirect&bpo=43931).)

- [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) along with its APIs now belong to the limited API as well as the stable ABI:

  - [`PyObject_CheckBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_CheckBuffer)

  - [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer)

  - [`PyBuffer_GetPointer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_GetPointer)

  - [`PyBuffer_SizeFromFormat()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_SizeFromFormat)

  - [`PyBuffer_ToContiguous()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_ToContiguous)

  - [`PyBuffer_FromContiguous()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FromContiguous)

  - [`PyObject_CopyData()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_CopyData)

  - [`PyBuffer_IsContiguous()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_IsContiguous)

  - [`PyBuffer_FillContiguousStrides()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FillContiguousStrides)

  - [`PyBuffer_FillInfo()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_FillInfo)

  - [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release)

  - [`PyMemoryView_FromBuffer()`](https://docs.python.org/3.14/c-api/memoryview.html#c.PyMemoryView_FromBuffer)

  - [`bf_getbuffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs.bf_getbuffer) and [`bf_releasebuffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer) type slots

(Contributed by Christian Heimes in [bpo-45459](https://bugs.python.org/issue?@action=redirect&bpo=45459).)

- Introduced the [`PyType_GetModuleByDef()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleByDef) function, which retrieves the module where a method was defined for those situations where that detail cannot be reached directly (through [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod)). (Contributed by Petr Viktorin in [bpo-46613](https://bugs.python.org/issue?@action=redirect&bpo=46613).)

-

Introduced fresh routines for packing and unpacking a C double (serializing and deserializing it): [`PyFloat_Pack2()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack2), [`PyFloat_Pack4()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack4), [`PyFloat_Pack8()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack8), [`PyFloat_Unpack2()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Unpack2), [`PyFloat_Unpack4()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Unpack4) and [`PyFloat_Unpack8()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Unpack8). (Contributed by Victor Stinner in [bpo-46906](https://bugs.python.org/issue?@action=redirect&bpo=46906).)

- Introduced fresh routines for reading frame object attributes: [`PyFrame_GetBuiltins()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBuiltins), [`PyFrame_GetGenerator()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGenerator), [`PyFrame_GetGlobals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGlobals), [`PyFrame_GetLasti()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLasti).

- Introduced a pair of fresh functions for reading and writing the currently handled exception instance: [`PyErr_GetHandledException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetHandledException) and [`PyErr_SetHandledException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetHandledException). They stand as substitutes for [`PyErr_SetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetExcInfo) and [`PyErr_GetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetExcInfo), which operate on the older 3-tuple form of exceptions. (Contributed by Irit Katriel in [bpo-46343](https://bugs.python.org/issue?@action=redirect&bpo=46343).)

- Introduced the [`PyConfig.safe_path`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.safe_path) member. (Contributed by Victor Stinner in [gh-57684](https://github.com/python/cpython/issues/57684).)

[Subject index](INDEX.md) · [Previous source section](build-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](c-api-trashcan-lifecycle-migration.md)
