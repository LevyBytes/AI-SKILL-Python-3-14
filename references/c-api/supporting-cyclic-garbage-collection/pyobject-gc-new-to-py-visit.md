# supporting cyclic garbage collection C API: `PyObject_GC_New`, `PyObject_GC_NewVar`, `PyType_GenericAlloc()`, `PyObject_GC_UnTrack()`, `Py_VISIT()`

`PyObject_GC_New`

- `PyObject_GC_NewVar`

- [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc)

- [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free)

 void PyObject_GC_UnTrack(void *op)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Take the object *op* out of the collector's set of tracked container objects. Mind that `PyObject_GC_Track()` may be called once more on this object to return it to the tracked set. The deallocator (the [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) handler) ought to call this on the object before any field the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler relies on turns invalid.

Changed in version 3.8: The `_PyObject_GC_TRACK()` and `_PyObject_GC_UNTRACK()` macros have been dropped from the public C API.

A function parameter of the following type is what the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler takes:

 typedef int (*visitproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object, void *arg)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type of the visitor function handed to the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler. You call it with the object to traverse as *object* and with the `tp_traverse` handler's third parameter as *arg*. Several visitor functions inside the Python core power cyclic garbage detection; ordinarily users have no need to author visitor functions of their own.

The [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handler is required to be of the following type:

 typedef int (*traverseproc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self, visitproc visit, void *arg)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The traversal function for a container object. An implementation has to call the *visit* function on every object held directly by *self*, passing *visit* both that contained object and the *arg* value the handler received. You must never call *visit* with a `NULL` object argument. Should *visit* yield a non-zero value, return that value right away.

A traversal function is barred from having side effects. An implementation may neither adjust the reference counts of any Python objects nor build or tear down any Python objects.

To ease the writing of [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handlers, a `Py_VISIT()` macro is on hand. Using it requires the `tp_traverse` implementation to name its arguments precisely *visit* and *arg*:

 Py_VISIT(o)

When the [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* *o* is not `NULL`, fire the *visit* callback with *o* and *arg* as its arguments; if *visit* yields a non-zero value, return it. With this macro in play, [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) handlers take this shape:

```c
static int
my_traverse(Noddy *self, visitproc visit, void *arg)
{
    Py_VISIT(self->foo);
    Py_VISIT(self->bar);
    return 0;
}

```

The [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) handler has to be of the `inquiry` type, or else `NULL` when the object is immutable.

 typedef int (*inquiry)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Let go of references that might have formed reference cycles. An immutable object need not define this method, since it can never directly form a reference cycle. Be aware the object still has to be valid once this method returns (do not merely call [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) on a reference). The collector invokes this method whenever it finds the object caught up in a reference cycle.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-tpflags-have-gc-to-pyobject-gc-newvar.md) · [Previous source contract](pyobject-newvar-to-pyobject-gc-del.md) · [Following source contract](pygc-collect-to-pygc-isenabled.md)
