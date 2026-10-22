# Defining `tp_dealloc`

#### Defining `tp_dealloc`

Should your type carry a custom [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) function, it must:

- invoke [`PyObject_GC_UnTrack()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_UnTrack) ahead of invalidating any fields, and

- lower the reference count of the type.

To keep the type alive across the `tp_free` call, decrement the type's refcount *after* the instance has been deallocated. For instance:

```c
static void my_dealloc(PyObject *self)
{
    PyObject_GC_UnTrack(self);
    ...
    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}

```

The standard `tp_dealloc` function already handles this, so when your type does *not* override `tp_dealloc` there is nothing to add.

[Subject index](INDEX.md) · [Previous source context](delegating-tp-traverse.md) · [Following source context](not-overriding-tp-free.md)
