# int PyCallable_Check(PyObject *o)

### Call Support API

 int PyCallable_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Work out whether object *o* can be called. Give back `1` when it is callable and `0` if it is not. Success is guaranteed for this routine.

[Subject index](INDEX.md) · [Previous source contract](pyobject-callmethod-to-pyobject-vectorcallmethod.md)
