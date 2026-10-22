# Python 3.12.0 alpha 1 / core and builtins / reflection

[gh-96975](https://github.com/python/cpython/issues/96975): Repair a crash that surfaced when [`PyEval_GetFrame()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetFrame) ran while the topmost Python frame sat in a partially-initialized state.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
