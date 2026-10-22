# Adding data and methods to the Basic example — Custom_init, PyObject, PyArg_ParseTupleAndKeywords, Py_INCREF, Py_XDECREF, tp_init, PyTypeObject, tp_new, tp_dealloc, PyMemberDef, Custom_members, Py_T_OBJECT_EX, Py_T_INT, tp_members

```c
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
    CustomObject *self = (CustomObject *) op;
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_XDECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_XDECREF(tmp);
    }
    return 0;
}

```

by populating the [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) slot.

```c
.tp_init = Custom_init,

```

Python surfaces the [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) slot as the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method. Its purpose is to set up an object once it has been created. Initializers always take positional and keyword arguments, and they ought to give back either `0` when they succeed or `-1` when something goes wrong.

In contrast to the `tp_new` handler, nothing guarantees that `tp_init` runs at all (the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module, for instance, normally skips calling [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) on unpickled instances). It may equally be invoked more than once. Nothing stops anyone from calling the `__init__()` method on our objects. That’s why we must be especially cautious as we set the new attribute values. One temptation, for example, would be to assign the `first` member this way:

```c
if (first) {
    Py_XDECREF(self->first);
    Py_INCREF(first);
    self->first = first;
}

```

That would court danger, however. Since our type places no restriction on the kind of object the `first` member holds, it might be any sort of object. Such an object could carry a destructor that runs code which goes on to read the `first` member; or that destructor might detach the [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) and permit arbitrary code in other threads to read and mutate our object.

Playing it safe and guarding against that scenario, we nearly always reassign members ahead of dropping their reference counts. So when can we skip that?

- whenever we are certain the reference count exceeds 1;

- whenever we know that releasing the object [1] will neither detach the [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) nor trigger any callbacks into our type’s code;

- whenever we’re decrementing a reference count inside a [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) handler belonging to a type that doesn’t take part in cyclic garbage collection [2].

We’d like to surface our instance variables as attributes. Several techniques exist for that. The most straightforward is to write member definitions:

```c
static PyMemberDef Custom_members[] = {
    {"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
     "first name"},
    {"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
     "last name"},
    {"number", Py_T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};

```

and lodge those definitions in the [`tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_members) slot:

[Subject index](INDEX.md) · [Previous source section](adding-data-and-methods-to-the-basic-example-and-tp-base.md) · [Next source section](custom-type-member-table-registration.md) · [Owning section and setup](adding-data-and-methods-to-the-basic-example.md)
