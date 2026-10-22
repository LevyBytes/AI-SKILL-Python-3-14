# Python 3.10.0 alpha 1 / library / ctypes

[bpo-40795](https://bugs.python.org/issue?@action=redirect&bpo=40795): For the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module: should ctypes fail to convert a callback's result, or should a ctypes callback function throw an exception, sys.unraisablehook now gets invoked with an exception set. Formerly, the error went to stderr through [`PyErr_Print()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Print).

[bpo-13097](https://bugs.python.org/issue?@action=redirect&bpo=13097): `ctypes` now throws an `ArgumentError` if a callback gets called with over 1024 arguments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
