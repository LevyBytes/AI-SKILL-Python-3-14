# Python 3.5.0 alpha 2 / core and builtins / exceptions and tracebacks

[bpo-23571](https://bugs.python.org/issue?@action=redirect&bpo=23571): When a function both hands back a result and triggers an exception, PyObject_Call() and PyCFunction_Call() will now flag a SystemError. That SystemError gets chained onto whatever exception came before it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
