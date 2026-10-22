# Python 3.14.0 alpha 1 / c api / reflection

[gh-122728](https://github.com/python/cpython/issues/122728): Patch [`PyEval_GetLocals()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetLocals) so it sidesteps [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) (?bad argument to internal function?). Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
