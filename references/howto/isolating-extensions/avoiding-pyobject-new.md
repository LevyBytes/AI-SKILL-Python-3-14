# Avoiding `PyObject_New`

#### Avoiding `PyObject_New`

Objects tracked by the GC have to be allocated with GC-aware functions.

When you reach for [`PyObject_New()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New) or [`PyObject_NewVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar):

- Fetch and invoke the type's [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot where you can. That means swapping `TYPE *o = PyObject_New(TYPE, typeobj)` for:

```c
TYPE *o = typeobj->tp_alloc(typeobj, 0);

```

Swap `o = PyObject_NewVar(TYPE, typeobj, size)` for the same form, but supply size in place of the 0.

- When that swap is not feasible (for instance within a custom `tp_alloc`), call [`PyObject_GC_New()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) or [`PyObject_GC_NewVar()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_NewVar):

```c
TYPE *o = PyObject_GC_New(TYPE, typeobj);

TYPE *o = PyObject_GC_NewVar(TYPE, typeobj, size);

```

[Subject index](INDEX.md) · [Previous source context](not-overriding-tp-free.md) · [Following source context](module-state-access-from-classes.md)
