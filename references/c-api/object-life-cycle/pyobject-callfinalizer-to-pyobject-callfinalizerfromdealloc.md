# Functions

### Functions

For allocating and releasing memory, consult [Allocating objects on the heap](https://docs.python.org/3.14/c-api/allocation.html#allocating-objects).

 void PyObject_CallFinalizer([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Finalizes the object in the manner laid out under [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize). Invoke this function (or `PyObject_CallFinalizerFromDealloc()`) rather than invoking `tp_finalize` on its own, since this function can collapse repeated calls to `tp_finalize` into one. For the moment, deduplication of calls happens only when the type supports garbage collection (that is, the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag is set); this could be revised later.

Added in version 3.4.

 int PyObject_CallFinalizerFromDealloc([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Behaves like `PyObject_CallFinalizer()` but is intended for invocation at the start of the object's destructor ([`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc)). No references to the object may exist. Should the object's finalizer resurrect the object, this function returns -1; no additional destruction ought to take place. Otherwise, this function returns 0 and destruction may proceed as usual.

Added in version 3.4.

See also

[`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) for example code.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](object-life-cycle.md) · [Previous source contract](cyclic-isolate-destruction.md)
