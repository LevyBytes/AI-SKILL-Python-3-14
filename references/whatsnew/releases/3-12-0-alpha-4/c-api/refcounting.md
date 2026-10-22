# Python 3.12.0 alpha 4 / c api / refcounting

[gh-98724](https://github.com/python/cpython/issues/98724): The [`Py_CLEAR`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR), [`Py_SETREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_SETREF) and [`Py_XSETREF`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XSETREF) macros each now evaluate their argument a single time. When an argument carries side effects, those side effects are no longer repeated. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
