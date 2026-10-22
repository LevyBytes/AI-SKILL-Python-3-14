# Python 3.13.0 alpha 2 / core and builtins / imports and modules

[gh-110543](https://github.com/python/cpython/issues/110543): Fix the Python 3.12 regression in which `types.CodeType.replace()` yielded a broken code object once invoked on a module- or class-level code object that holds a comprehension. Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
