# Python 3.14.0 alpha 4 / core and builtins / exceptions

[gh-128079](https://github.com/python/cpython/issues/128079): Correct a defect in which [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star) failed to validate what an [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup)'s [`split()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.split) handed back, which could crash the interpreter under certain conditions. Should `split()` hand over an invalid object, `except*` now raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and chains the originally raised `ExceptionGroup` object to it.

[gh-128078](https://github.com/python/cpython/issues/128078): Resolved a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) triggered by calling [`anext()`](https://docs.python.org/3.14/library/functions.html#anext) with a default tuple value. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
