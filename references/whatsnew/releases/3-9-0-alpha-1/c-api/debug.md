# Python 3.9.0 alpha 1 / c api / debug

[bpo-36389](https://bugs.python.org/issue?@action=redirect&bpo=36389): The `_PyObject_CheckConsistency()` function now exists in release mode too. As one use, it helps debug a crash inside the GC's `visit_decref()` function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
