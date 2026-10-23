# Subclassing list with SubList - PyListObject, PyObject_HEAD, PyObject, SubList_init, PyList_Type, tp_init, tp_new, PyTypeObject, tp_dealloc, tp_alloc, tp_base, Py_mod_exec, PyType_Ready, PyModule_AddObjectRef, PyType_GenericNew

```c
typedef struct {
    PyListObject list;
    int state;
} SubListObject;

```

What chiefly sets a derived type object apart is the requirement that the object layout of the base type appear as the leading member. That base type already carries the [`PyObject_HEAD()`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD) right at the top of its own structure.

Given a Python object that happens to be a `SubList` instance, you may cast its `PyObject *` pointer without risk to either `PyListObject *` or `SubListObject *`:

```c
static int
SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
{
    SubListObject *self = (SubListObject *) op;
    if (PyList_Type.tp_init(op, args, kwds) < 0)
        return -1;
    self->state = 0;
    return 0;
}

```

The snippet above demonstrates the way to forward a call into the base type's [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method.

Following this pattern matters whenever you author a type carrying custom [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) and [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) members. Rather than allocating the object's storage itself through [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc), the `tp_new` handler ought to defer that work to the base class by invoking the base class's own `tp_new`.

Within the [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) struct there is a [`tp_base`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_base) that names the concrete base class for the type. Because compilers across platforms behave inconsistently, you cannot populate that slot outright with a reference to [`PyList_Type`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Type); instead, handle it inside the [`Py_mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function:

```c
static int
sublist_module_exec(PyObject *m)
{
    SubListType.tp_base = &PyList_Type;
    if (PyType_Ready(&SubListType) < 0) {
        return -1;
    }

    if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
        return -1;
    }

    return 0;
}

```

Ahead of any [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) call, make sure the [`tp_base`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_base) slot of the type structure has been set. Since we are subclassing a type that already exists, there is no need to populate the [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot using [`PyType_GenericNew()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericNew) – the allocator gets inherited straight from the base type.

From there, the steps of invoking [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) and registering the type object on the module proceed exactly as they did for the elementary `Custom` examples.

Footnotes

[Subject index](INDEX.md) · [Previous source section](subclassing-list-with-sublist-and-pymoduledef-init.md) · [Owning section and setup](subclassing-list-with-sublist-and-pymoduledef-init.md) · [Preceding cross-file owner and contract](subclassing-other-types-pytypeobject.md)
