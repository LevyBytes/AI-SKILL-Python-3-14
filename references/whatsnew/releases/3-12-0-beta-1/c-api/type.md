# Python 3.12.0 beta 1 / c api / type

[gh-103968](https://github.com/python/cpython/issues/103968): [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), together with its variants, now permits building classes whose metaclass supplies its own [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new). That `tp_new` gets ignored. This conduct is deprecated and slated to be forbidden in 3.14+. The newer [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass) forbids it already.

[gh-103509](https://github.com/python/cpython/issues/103509): Added a C API for subclassing types whose instance memory layout stays opaque: [`PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize) may now be zero or below zero, [`PyObject_GetTypeData()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetTypeData) fetches subclass-specific data, and [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END) safely extends variable-size objects. Consult [**PEP 697**](https://peps.python.org/pep-0697/) for the specifics.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
