# Python 3.10.0 beta 1 / library / io

[bpo-43680](https://bugs.python.org/issue?@action=redirect&bpo=43680): The Python `_pyio.open()` function turns into a static method so it mirrors the [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) built-in function: it will not turn into a bound method once kept in a class variable. That is feasible now that static methods became callable in Python 3.10. On top of that, `_pyio.OpenWrapper()` is reduced to a plain alias for `_pyio.open()`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
