# Python 3.10.0 alpha 6 / c api / iter

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): To keep implementation details hidden, [`PyIter_Check()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Check) is from now on declared exclusively as a function. Previously the macro reached straight into [`PyTypeObject.tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext). Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
