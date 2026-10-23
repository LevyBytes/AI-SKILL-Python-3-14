# Supporting cyclic garbage collection - Custom_traverse, PyObject, Py_VISIT, tp_traverse, PyTypeObject, Custom_clear, Py_CLEAR, Py_XDECREF, Custom_dealloc, PyObject_GC_UnTrack

To begin, the traversal method informs the cyclic GC about the subobjects that might take part in cycles:

```c
static int
Custom_traverse(PyObject *op, visitproc visit, void *arg)
{
    CustomObject *self = (CustomObject *) op;
    int vret;
    if (self->first) {
        vret = visit(self->first, arg);
        if (vret != 0)
            return vret;
    }
    if (self->last) {
        vret = visit(self->last, arg);
        if (vret != 0)
            return vret;
    }
    return 0;
}

```

Every subobject capable of joining a cycle requires that we invoke the `visit()` function, which the traversal method receives as a parameter. Two things are passed to `visit()`: the subobject plus the supplementary argument *arg* that the traversal method was given. It hands back an integer, and that value has to be returned whenever it is non-zero.

To handle the calling of visit functions automatically, Python offers a [`Py_VISIT()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.Py_VISIT) macro. By using `Py_VISIT()`, the boilerplate inside `Custom_traverse` shrinks to a minimum:

```c
static int
Custom_traverse(PyObject *op, visitproc visit, void *arg)
{
    CustomObject *self = (CustomObject *) op;
    Py_VISIT(self->first);
    Py_VISIT(self->last);
    return 0;
}

```

Note

To be able to use [`Py_VISIT()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.Py_VISIT), the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) implementation is required to label its arguments precisely *visit* and *arg*.

Next, a method is needed for wiping any subobjects that might be involved in cycles:

```c
static int
Custom_clear(PyObject *op)
{
    CustomObject *self = (CustomObject *) op;
    Py_CLEAR(self->first);
    Py_CLEAR(self->last);
    return 0;
}

```

Observe how the [`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR) macro is applied. This is the endorsed, safe technique for clearing data attributes of any type while lowering their reference counts. Should you instead invoke [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) on the attribute before resetting it to `NULL`, the attribute's destructor might re-enter code that reads that attribute once more (*particularly* when a reference cycle exists).

Note

[`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR) could be imitated by writing:

```c
PyObject *tmp;
tmp = self->first;
self->first = NULL;
Py_XDECREF(tmp);

```

Even so, reaching for [`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR) every time you delete an attribute is far simpler and far less prone to mistakes. Resist micro-optimizing if it costs you robustness!

While clearing attributes, the deallocator `Custom_dealloc` may run arbitrary code. That means the circular GC could fire from inside the function. Because the GC presumes the reference count is non-zero, we have to untrack the object from the GC via [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack) before any members are cleared. Below is our rewritten deallocator that relies on `PyObject_GC_UnTrack()` and `Custom_clear`:

[Subject index](INDEX.md) · [Previous source section](supporting-cyclic-garbage-collection-and-pyinit-custom4.md) · [Next source section](supporting-cyclic-garbage-collection-and-pytypeobject.md) · [Owning section and setup](supporting-cyclic-garbage-collection.md)
