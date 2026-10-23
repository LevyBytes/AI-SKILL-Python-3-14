# Providing finer control over data attributes - PyObject, Custom_getfirst, Py_INCREF, Custom_setfirst, PyErr_SetString, PyExc_TypeError, PyUnicode_Check, Py_DECREF, PyGetSetDef, Custom_getsetters, Custom_getlast, Custom_setlast, tp_getset, PyTypeObject, PyMemberDef, Custom_members, Py_T_INT, tp_init

For tighter governance over the `first` and `last` attributes, we'll supply our own getter and setter functions. Below are the routines that get and set the `first` attribute:

```c
static PyObject *
Custom_getfirst(PyObject *op, void *closure)
{
    CustomObject *self = (CustomObject *) op;
    Py_INCREF(self->first);
    return self->first;
}

static int
Custom_setfirst(PyObject *op, PyObject *value, void *closure)
{
    CustomObject *self = (CustomObject *) op;
    PyObject *tmp;
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The first attribute value must be a string");
        return -1;
    }
    tmp = self->first;
    Py_INCREF(value);
    self->first = value;
    Py_DECREF(tmp);
    return 0;
}

```

Two things reach the getter function: a `Custom` object and a "closure" that takes the form of a void pointer. Here that closure goes unused. (The closure enables an advanced pattern where definition data is handed to the getter and setter. One could leverage this, say, so that a single pair of getter and setter functions selects which attribute to read or write according to data carried in the closure.)

What arrives at the setter function is the `Custom` object, the incoming value, and the closure. That new value might be `NULL`, signaling that the attribute is being removed. Our setter raises an error whenever the attribute is deleted or whenever the supplied value isn't a string.

We assemble an array of [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) structures:

```c
static PyGetSetDef Custom_getsetters[] = {
    {"first", Custom_getfirst, Custom_setfirst,
     "first name", NULL},
    {"last", Custom_getlast, Custom_setlast,
     "last name", NULL},
    {NULL}  /* Sentinel */
};

```

and we record it within the [`tp_getset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_getset) slot:

```c
.tp_getset = Custom_getsetters,

```

That final field in a [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) structure is the "closure" referenced earlier. Since no closure is in play here, we simply supply `NULL`.

The member definitions for these attributes are dropped as well:

```c
static PyMemberDef Custom_members[] = {
    {"number", Py_T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};

```

The [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) handler also has to be revised so that only strings [3] are accepted:

[Subject index](INDEX.md) · [Previous source section](managed-attributes-module-initialization.md) · [Next source section](providing-finer-control-over-data-attributes-and-tp-new.md) · [Owning section and setup](providing-finer-control-over-data-attributes.md)
