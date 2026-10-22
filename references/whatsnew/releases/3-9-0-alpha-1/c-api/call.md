# Python 3.9.0 alpha 1 / c api / call

[bpo-29548](https://bugs.python.org/issue?@action=redirect&bpo=29548): These functions — `PyEval_CallObject`, `PyEval_CallFunction`, `PyEval_CallMethod` and `PyEval_CallObjectWithKeywords` — are deprecated. Reach for [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) and its variants instead.

[bpo-37151](https://bugs.python.org/issue?@action=redirect&bpo=37151): `PyCFunction_Call` is now a deprecated alias of [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call).

[bpo-37194](https://bugs.python.org/issue?@action=redirect&bpo=37194): A fresh public [`PyObject_CallNoArgs()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallNoArgs) entry point joins the C API for invoking a callable Python object with zero arguments. For dispatching a no-argument callback it is the leanest route. Take x86-64, for example: each `PyObject_CallFunctionObjArgs(func, NULL)` invocation reserves 960 bytes of stack, while `PyObject_CallNoArgs(func)` consumes just 624 bytes apiece.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
