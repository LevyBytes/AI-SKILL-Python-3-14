# Python 3.12.0 alpha 1 / core and builtins / threads

[gh-96071](https://github.com/python/cpython/issues/96071): Repair a deadlock inside [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) that occurred while allocating a new thread state. Kumar Aditya wrote the patch.

[gh-95818](https://github.com/python/cpython/issues/95818): Step past incomplete frames within [`PyThreadState_GetFrame()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetFrame).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
