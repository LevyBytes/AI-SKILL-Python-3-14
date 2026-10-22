# Python 3.9.0 beta 1 / c api / type

[bpo-40217](https://bugs.python.org/issue?@action=redirect&bpo=40217): Make certain that objects of types built via [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) visit their class object as the garbage collector walks references (done as an extension to the supplied [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse)). Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
