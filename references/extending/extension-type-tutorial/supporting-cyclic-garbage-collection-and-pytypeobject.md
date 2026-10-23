# Supporting cyclic garbage collection - Custom_dealloc, PyObject, PyObject_GC_UnTrack, Custom_clear, Py_TYPE, tp_free, Py_TPFLAGS_HAVE_GC, tp_flags, Py_TPFLAGS_DEFAULT, Py_TPFLAGS_BASETYPE, tp_alloc, PyTypeObject

```c
static void
Custom_dealloc(PyObject *op)
{
    PyObject_GC_UnTrack(op);
    (void)Custom_clear(op);
    Py_TYPE(op)->tp_free(op);
}

```

To wrap up, we attach the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC) flag to the class flags:

```c
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,

```

That covers nearly everything. Had we supplied custom [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) or [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) handlers, we'd have to adjust them for cyclic garbage collection. The majority of extensions simply rely on the automatically supplied versions.

[Subject index](INDEX.md) · [Previous source section](supporting-cyclic-garbage-collection-and-pyobject-gc-untrack.md) · [Next source section](subclassing-other-types-pytypeobject.md) · [Owning section and setup](supporting-cyclic-garbage-collection.md)
