# Python 3.10.0 alpha 6 / c api / descriptor

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): The [`PyDescr_IsData()`](https://docs.python.org/3.14/c-api/descriptor.html#c.PyDescr_IsData) macro became a function so implementation details stay hidden: the macro had reached straight into [`PyTypeObject.tp_descr_set`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_descr_set). Erlend E. Aasland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
