# Python 3.9.0 alpha 5 / c api / exceptions and tracebacks

[bpo-38913](https://bugs.python.org/issue?@action=redirect&bpo=38913): Repaired a segfault in `Py_BuildValue()` when it was invoked with a format that contains "#" and PY_SSIZE_T_CLEAN was undefined whwn an exception is set.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
