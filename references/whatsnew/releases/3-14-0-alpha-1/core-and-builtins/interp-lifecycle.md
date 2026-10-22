# Python 3.14.0 alpha 1 / core and builtins / interp lifecycle

[gh-123022](https://github.com/python/cpython/issues/123022): Stop the free-threaded build from crashing when [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) is invoked off a non-main thread.

[gh-120838](https://github.com/python/cpython/issues/120838): Both [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) and [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) now always operate with the main interpreter active.

[gh-113190](https://github.com/python/cpython/issues/113190): [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) now wipes out every interned string.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
