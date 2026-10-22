# Python 3.13.0 alpha 1 / c api / functions and types

[gh-105182](https://github.com/python/cpython/issues/105182): The `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` functions, which Python 3.2 deprecated, are removed. Victor Stinner wrote the patch.

[gh-105182](https://github.com/python/cpython/issues/105182): The `PyEval_InitThreads()` and `PyEval_ThreadsInitialized()` functions, which Python 3.9 deprecated, are removed. Victor Stinner wrote the patch.

[gh-105156](https://github.com/python/cpython/issues/105156): The old `Py_UNICODE` and `PY_UNICODE_TYPE` types are deprecated; reach for the `wchar_t` type directly instead. Ever since Python 3.3, `Py_UNICODE` and `PY_UNICODE_TYPE` have merely aliased `wchar_t`. Victor Stinner wrote the patch.

[gh-107915](https://github.com/python/cpython/issues/107915): C API functions like `PyErr_SetString()`, `PyErr_Format()`, `PyErr_SetFromErrnoWithFilename()` plus many more no longer crash or swallow errors should they fail to format the message or decode the filename. They retain a matching error instead.

[gh-108765](https://github.com/python/cpython/issues/108765): The `<ieeefp.h>` standard header is no longer pulled in by `Python.h`. It had been there for the `finite()` function, which the `<math.h>` header now supplies. Include it directly when needed. The `HAVE_IEEEFP_H` macro is also dropped. Victor Stinner wrote the patch.

[gh-108337](https://github.com/python/cpython/issues/108337): Atomic operations covering more data types are added in pyatomic.h.

[gh-105115](https://github.com/python/cpython/issues/105115): For builtin static types, `PyTypeObject.tp_bases` (along with `tp_mro`) are now shared across every interpreter, whereas 3.12-beta1 had kept them on `PyInterpreterState`. Note as well that the tuples are now immortal objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
