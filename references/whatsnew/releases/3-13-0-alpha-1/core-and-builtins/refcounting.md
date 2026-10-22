# Python 3.13.0 alpha 1 / core and builtins / refcounting

[gh-109496](https://github.com/python/cpython/issues/109496): On a debug-mode Python build, [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) now invokes `_Py_NegativeRefcount()` when the object is a dangling pointer into freed memory: storage that the debug hook on memory allocators has stuffed with the `0xDD` "dead byte". The remedy is to inspect the reference count *before* the test for `_Py_IsImmortal()`. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
