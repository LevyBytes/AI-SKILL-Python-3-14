# Python 3.14.0 alpha 1 / c api / type

[gh-124153](https://github.com/python/cpython/issues/124153): Introduce [`PyType_GetBaseByToken()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetBaseByToken) along with the [`Py_tp_token`](https://docs.python.org/3.14/c-api/type.html#c.Py_tp_token) slot to simplify type checking, tied to [**PEP 489**](https://peps.python.org/pep-0489/) and [**PEP 630**](https://peps.python.org/pep-0630/).

[gh-123909](https://github.com/python/cpython/issues/123909): [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases), and [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) from now on fail whenever the new type's metaclass carries a custom [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
