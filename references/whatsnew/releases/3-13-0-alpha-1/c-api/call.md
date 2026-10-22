# Python 3.13.0 alpha 1 / c api / call

[gh-105107](https://github.com/python/cpython/issues/105107): Functions that Python 3.9 deprecated are removed.

  - `PyEval_CallObject()`, `PyEval_CallObjectWithKeywords()`: use [`PyObject_CallNoArgs()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallNoArgs) and [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) (positional arguments must not be *NULL*) instead.

  - `PyEval_CallFunction()`: use [`PyObject_CallFunction()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallFunction) instead.

  - `PyEval_CallMethod()`: use [`PyObject_CallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_CallMethod) instead.

  - `PyCFunction_Call()`: use [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) instead.

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
