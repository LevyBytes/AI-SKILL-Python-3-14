# Python 3.13.0 alpha 6 / c api / constants

[gh-115754](https://github.com/python/cpython/issues/115754): Within the limited C API version 3.13, fetching the `Py_None`, `Py_False`, `Py_True`, `Py_Ellipsis` and `Py_NotImplemented` singletons now happens through function calls at the stable ABI level, which hides the implementation details. Those constants are still returned as borrowed references. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
