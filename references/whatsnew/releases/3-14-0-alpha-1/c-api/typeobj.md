# Python 3.14.0 alpha 1 / c api / typeobj

[gh-119775](https://github.com/python/cpython/issues/119775): Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) atop mutable bases had been deprecated as of 3.12 and now triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[gh-100554](https://github.com/python/cpython/issues/100554): Introduced a `Py_tp_vectorcall` slot for assigning [`tp_vectorcall`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall) by way of the [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec) function family. Through this feature, Limited API extensions gain a more efficient vector-call-based implementation of `__new__` and `__init__`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
