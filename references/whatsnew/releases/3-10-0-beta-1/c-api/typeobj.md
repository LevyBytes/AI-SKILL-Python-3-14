# Python 3.10.0 beta 1 / c api / typeobj

[bpo-43916](https://bugs.python.org/issue?@action=redirect&bpo=43916): A new [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION) type flag was added to forbid creating instances of a type. Victor Stinner supplied the patch.

[bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908): A [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) flag was introduced for immutable type objects, and [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) was changed to apply it to static types. Erlend E. Aasland supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
