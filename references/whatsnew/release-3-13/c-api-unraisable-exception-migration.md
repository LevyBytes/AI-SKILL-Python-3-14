# Python 3.13 changes: Public replacements for unraisable-error and internal helpers

- `_PyErr_WriteUnraisableMsg()`: [`PyErr_FormatUnraisable()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_FormatUnraisable);

  - `_PyEval_SetTrace()`: [`PyEval_SetTrace()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTrace) or [`PyEval_SetTraceAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTraceAllThreads);

  - `_PyList_Extend()`: [`PyList_Extend()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Extend);

  - `_PyLong_AsInt()`: [`PyLong_AsInt()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt);

  - `_PyMem_RawStrdup()`: `strdup()`;

  - `_PyMem_Strdup()`: `strdup()`;

  - `_PyObject_ClearManagedDict()`: [`PyObject_ClearManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_ClearManagedDict);

  - `_PyObject_VisitManagedDict()`: [`PyObject_VisitManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_VisitManagedDict);

  - `_PyThreadState_UncheckedGet()`: [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked);

  - `_PyTime_AsSecondsDouble()`: [`PyTime_AsSecondsDouble()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_AsSecondsDouble);

  - `_PyTime_GetMonotonicClock()`: [`PyTime_Monotonic()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Monotonic) or [`PyTime_MonotonicRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MonotonicRaw);

  - `_PyTime_GetPerfCounter()`: [`PyTime_PerfCounter()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_PerfCounter) or [`PyTime_PerfCounterRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_PerfCounterRaw);

  - `_PyTime_GetSystemClock()`: [`PyTime_Time()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Time) or [`PyTime_TimeRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_TimeRaw);

  - `_PyTime_MAX`: [`PyTime_MAX`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MAX);

  - `_PyTime_MIN`: [`PyTime_MIN`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MIN);

  - `_PyTime_t`: [`PyTime_t`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_t);

  - `_Py_HashPointer()`: [`Py_HashPointer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashPointer);

  - `_Py_IsFinalizing()`: [`Py_IsFinalizing()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IsFinalizing).

To pull most of these new functions into Python 3.12 and earlier, you can rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/).

[Subject index](INDEX.md) · [Previous source section](c-api-trashcan-migration.md) · [Next source section](regression-test-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-13.md) · [Release/subject declaration](c-api-trashcan-migration.md)
