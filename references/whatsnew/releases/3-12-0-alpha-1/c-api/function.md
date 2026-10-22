# Python 3.12.0 alpha 1 / c api / function

[gh-92193](https://github.com/python/cpython/issues/92193): Introduce a fresh [`PyFunction_SetVectorcall()`](https://docs.python.org/3.14/c-api/function.html#c.PyFunction_SetVectorcall) function into the C API; it assigns the vectorcall field on any supplied [`PyFunctionObject`](https://docs.python.org/3.14/c-api/function.html#c.PyFunctionObject).

Warning: an extension wielding this API has to keep the original function's behavior intact!

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
