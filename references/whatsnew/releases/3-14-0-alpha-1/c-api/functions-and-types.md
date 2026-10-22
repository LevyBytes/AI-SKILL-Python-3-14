# Python 3.14.0 alpha 1 / c api / functions and types

[gh-119336](https://github.com/python/cpython/issues/119336): Bring back the `_PyLong_NumBits()` function that had been removed. The pywin32 project relies on it. Ethan Smith wrote the patch.

[gh-120642](https://github.com/python/cpython/issues/120642): Take the private `_Py_CODEUNIT` type out of the public C API. From now on the internal `pycore_code.h` header is where you get this internal type. Victor Stinner wrote the patch.

[gh-120642](https://github.com/python/cpython/issues/120642): Take out these unstable functions:

  - `PyUnstable_Replace_Executor()`

  - `PyUnstable_SetOptimizer()`

  - `PyUnstable_GetOptimizer()`

  - `PyUnstable_GetExecutor()`

  - `PyUnstable_Optimizer_NewCounter()`

  - `PyUnstable_Optimizer_NewUOpOptimizer()`

Victor Stinner wrote the patch.

[gh-112136](https://github.com/python/cpython/issues/112136): Bring back the private `_PyArg_Parser` structure together with the private `_PyArg_ParseTupleAndKeywordsFast()` function, both pulled earlier in Python 3.13 alpha 1. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
