# Weak Reference Support — Py_TPFLAGS_MANAGED_WEAKREF, tp_flags, PyTypeObject, tp_weaklistoffset, PyVarObject_HEAD_INIT, tp_dealloc, PyObject_ClearWeakRefs, PyObject, Py_TYPE, tp_free

### 3.6. Weak Reference Support

A design aim behind Python's weak reference implementation is to let any type take part in the weak reference mechanism while sparing performance-critical objects (numbers, for instance) from bearing the overhead.

See also

Reference material covering the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module.

To make an object eligible for weak referencing, the extension type has to turn on the `Py_TPFLAGS_MANAGED_WEAKREF` bit within its [`tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags) field. As for the older [`tp_weaklistoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset) field, leave it at zero.

In concrete terms, the statically declared type object would take this shape:

```c
static PyTypeObject TrivialType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    /* ... other members omitted for brevity ... */
    .tp_flags = Py_TPFLAGS_MANAGED_WEAKREF | ...,
};

```

The sole remaining piece to add is that `tp_dealloc` must clear out any weak references, which it does by calling [`PyObject_ClearWeakRefs()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyObject_ClearWeakRefs):

```c
static void
Trivial_dealloc(PyObject *op)
{
    /* Clear weakrefs first before calling any destructors */
    PyObject_ClearWeakRefs(op);
    /* ... remainder of destruction code omitted for brevity ... */
    Py_TYPE(op)->tp_free(op);
}

```

[Subject index](INDEX.md) · [Previous source section](call-and-iterator-protocol-slots-and-pytypeobject.md) · [Next source section](rich-comparison-and-type-checking.md)
