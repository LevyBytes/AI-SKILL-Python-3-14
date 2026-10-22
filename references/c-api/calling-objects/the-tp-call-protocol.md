# The tp_call Protocol

### The *tp_call* Protocol

A class becomes callable once its instances populate [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call). Here is what that slot's signature looks like:

```c
PyObject *tp_call(PyObject *callable, PyObject *args, PyObject *kwargs);

```

Invoking a call relies on a tuple to carry the positional arguments and a dict to carry the keyword arguments, paralleling how `callable(*args, **kwargs)` behaves in Python source. *args* has to be non-NULL — supply an empty tuple when nothing is passed — whereas *kwargs* is permitted to be *NULL* when no keyword arguments exist.

It is not solely *tp_call* that follows this scheme: [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) plus [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) hand off their arguments identically.

Reach for `PyObject_Call()` or some other call API whenever you need to invoke an object.

[Subject index](INDEX.md) · [Previous source contract](call-protocol.md) · [Following source contract](pyobject.md)
