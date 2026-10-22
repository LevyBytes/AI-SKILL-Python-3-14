# Delegating `tp_traverse`

#### Delegating `tp_traverse`

Where your traverse function hands off to the [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) of its base class (or some other type), make sure `Py_TYPE(self)` gets visited a single time only. Note that only a heap type is meant to visit the type within `tp_traverse`.

For instance, suppose your traverse function contains:

```c
base->tp_traverse(self, visit, arg)

```

?and `base` could be a static type, then it ought to additionally contain:

```c
if (base->tp_flags & Py_TPFLAGS_HEAPTYPE) {
    // a heap type's tp_traverse already visited Py_TYPE(self)
} else {
    if (Py_Version >= 0x03090000) {
        Py_VISIT(Py_TYPE(self));
    }
}

```

There is no need to manage the type's reference count within [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) and [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear).

[Subject index](INDEX.md) · [Previous source context](tp-traverse-in-python-3-8-and-lower.md) · [Following source context](defining-tp-dealloc.md)
