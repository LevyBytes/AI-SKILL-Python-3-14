# Python 3.13 changes: Removed thread initialization and internal helper APIs

Drop the `PyEval_ThreadsInitialized()` function, which carried a deprecation back in Python 3.9. From Python 3.7 onward, `Py_Initialize()` always sets up the GIL, so `PyEval_InitThreads()` is a no-op and `PyEval_ThreadsInitialized()` returns non-zero in every case. (Contributed by Victor Stinner in [gh-105182](https://github.com/python/cpython/issues/105182).)

- Drop the `_PyInterpreterState_Get()` alias for [`PyInterpreterState_Get()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState_Get), retained earlier so code stayed compatible with Python 3.8. To obtain `PyInterpreterState_Get()` on Python 3.8 and earlier, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/). (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320).)

- Drop the private `_PyObject_FastCall()` function; reach for `PyObject_Vectorcall()`, which has shipped since Python 3.8 ([**PEP 590**](https://peps.python.org/pep-0590/)). (Contributed by Victor Stinner in [gh-106023](https://github.com/python/cpython/issues/106023).)

- Drop the `cpython/pytime.h` header file, whose contents were entirely private functions. (Contributed by Victor Stinner in [gh-106316](https://github.com/python/cpython/issues/106316).)

- Drop the undocumented `PY_TIMEOUT_MAX` constant out of the limited C API. (Contributed by Victor Stinner in [gh-110014](https://github.com/python/cpython/issues/110014).)

- Drop the old trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END`. Swap in the newer pair `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END` for both. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111).)

[Subject index](INDEX.md) · [Next source section](c-api-changes-deprecated-c-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-removed-c-apis.md) · [Preceding release/subject continuation](c-api-changes-removed-c-apis.md)
