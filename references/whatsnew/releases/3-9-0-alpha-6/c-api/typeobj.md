# Python 3.9.0 alpha 6 / c api / typeobj

[bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170): Turn the `PyObject_GET_WEAKREFS_LISTPTR()` macro into a function so implementation details stay hidden: that macro had been reaching straight into the [`PyTypeObject.tp_weaklistoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset) member.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
