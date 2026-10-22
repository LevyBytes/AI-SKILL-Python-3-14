# Custom type members and methods — PyObject, Custom_name, Py_UNUSED, PyErr_SetString, PyExc_AttributeError, PyUnicode_FromFormat, PyMethodDef, Custom_methods, tp_methods, PyTypeObject, Py_TPFLAGS_BASETYPE, tp_flags, Py_TPFLAGS_DEFAULT, PyInit_custom, PyInit_custom2, PyModuleDef

Every member entry carries a name, a type, an offset, access flags, and a documentation string. For the specifics, consult the [Generic Attribute Management](https://docs.python.org/3.14/extending/newtypes.html#generic-attribute-management) section further down.

One drawback here is that nothing constrains which object types may be stored in the Python attributes. While strings are what we anticipate for the first and last names, callers are free to assign arbitrary Python objects instead. On top of that, the attributes are deletable, which leaves the C pointers pointing at `NULL`. So even after we guarantee the members start out as non-`NULL` values, deleting the attributes can still reset those members back to `NULL`.

A lone method, `Custom.name()`, is defined here; it emits the object's name by joining the first and last names together.

```c
static PyObject *
Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
{
    CustomObject *self = (CustomObject *) op;
    if (self->first == NULL) {
        PyErr_SetString(PyExc_AttributeError, "first");
        return NULL;
    }
    if (self->last == NULL) {
        PyErr_SetString(PyExc_AttributeError, "last");
        return NULL;
    }
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
}

```

This is coded as a C function whose first parameter receives a `Custom` instance (or one from a `Custom` subclass). The leading argument to a method is invariably the instance itself. Although methods frequently accept positional and keyword arguments too, here we accept none, so neither a positional argument tuple nor a keyword argument dictionary is required. The Python equivalent of this method reads:

```python
def name(self):
    return "%s %s" % (self.first, self.last)

```

Keep in mind that we must guard against our `first` and `last` members being `NULL`. They can, after all, be deleted, and deletion sets them to `NULL`. A cleaner design would forbid deleting these attributes and would confine their values to strings. The following section demonstrates exactly how that is accomplished.

Having defined the method, our next step is to build an array holding the method definitions:

```c
static PyMethodDef Custom_methods[] = {
    {"name", Custom_name, METH_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /* Sentinel */
};

```

(observe that the [`METH_NOARGS`](https://docs.python.org/3.14/c-api/structures.html#c.METH_NOARGS) flag here signals that the method takes no arguments beyond *self*)

and we hand it off to the [`tp_methods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_methods) slot:

```c
.tp_methods = Custom_methods,

```

As a last step, we make the type subclassable so it can serve as a base class. Up to now our methods have been authored with care, avoiding any assumptions about what type of object is being constructed or operated on, so the only remaining task is appending [`Py_TPFLAGS_BASETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_BASETYPE) to the class flag definition:

```c
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,

```

`PyInit_custom()` becomes `PyInit_custom2()`, the module name within the [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) struct is revised, and the complete class name inside the [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) struct is updated as well.

To finish, our `setup.py` file gains an entry for the new module,

```python
from setuptools import Extension, setup
setup(ext_modules=[
    Extension("custom", ["custom.c"]),
    Extension("custom2", ["custom2.c"]),
])

```

after which a fresh install lets us `import custom2`:

[Subject index](INDEX.md) · [Next source section](custom-type-members-and-methods.md) · [Preceding cross-file owner and contract](adding-data-and-methods-to-the-basic-example.md) · [Immediate preceding contract and example context](custom-type-member-table-registration.md)
