# Python 3.12.0 alpha 2 / core and builtins / call

[gh-98586](https://github.com/python/cpython/issues/98586): The [`PyObject_Vectorcall()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Vectorcall) and [`PyObject_VectorcallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_VectorcallMethod) methods were added to the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable), accompanied by the helper macro constant [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3.14/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET).

Having these functions on hand makes faster [**PEP 590**](https://peps.python.org/pep-0590/) vector calls possible from compiled extension modules, sidestepping the cost of boxing and unboxing arguments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
