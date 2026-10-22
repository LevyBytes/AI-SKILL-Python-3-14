# Python 3.9.0 alpha 5 / c api / functions and types

[bpo-37207](https://bugs.python.org/issue?@action=redirect&bpo=37207): Provide the _PyArg_NoKwnames helper function. Donghee Na supplied the patch.

[bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947): Relocate the static inline function variants of Py_EnterRecursiveCall() and Py_LeaveRecursiveCall() into the internal C API, since they touch PyThreadState attributes. Ordinary functions that conceal implementation details are offered by the limited C API.

[bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947): The Py_TRASHCAN_BEGIN_CONDITION and Py_TRASHCAN_END macro no longer reach into PyThreadState attributes; instead they invoke the new private _PyTrash_begin() and _PyTrash_end() functions, which conceal implementation details.

[bpo-39877](https://bugs.python.org/issue?@action=redirect&bpo=39877): The `PyEval_InitThreads()` and `PyEval_ThreadsInitialized()` functions were deprecated. A `PyEval_InitThreads()` call now has no effect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
