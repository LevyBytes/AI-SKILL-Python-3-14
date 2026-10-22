# Python 3.13.0 alpha 3 / core and builtins / imports and modules

[gh-112716](https://github.com/python/cpython/issues/112716): Resolved a SystemError occurring in the `import` statement and within the `__reduce__()` methods of builtin types whenever `__builtins__` is not a dict.

[gh-112660](https://github.com/python/cpython/issues/112660): Refrain from clearing unexpected errors while formatting the error messages for ImportError and AttributeError on modules.

[gh-95754](https://github.com/python/cpython/issues/95754): Deliver a clearer error message upon accessing invalid attributes on partially initialized modules. The message now carries the origin of the accessed module to assist with the frequent issue of shadowing other modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
