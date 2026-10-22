# Python 3.10.0 alpha 1 / c api / arg

[bpo-40943](https://bugs.python.org/issue?@action=redirect&bpo=40943): To use [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) formats that employ `#` — namely `es#`, `et#`, `s#`, `u#`, `y#`, `z#`, `U#` and `Z#` — the `PY_SSIZE_T_CLEAN` macro now has to be defined. Consult [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) along with [**PEP 353**](https://peps.python.org/pep-0353/).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
