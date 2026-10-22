# Python 3.14.0 beta 3 / core and builtins / stdtypes

[gh-132617](https://github.com/python/cpython/issues/132617): A [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) modification check was fixed; it could wrongly raise a “dict mutated during update” error whenever a different dictionary, one that happens to share the same underlying keys object, was modified.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
