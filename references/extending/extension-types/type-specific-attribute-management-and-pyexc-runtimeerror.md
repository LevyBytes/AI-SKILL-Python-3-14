# Type-specific Attribute Management - PyObject, tp_getattr, PyTypeObject, PyLong_FromLong, PyErr_Format, PyExc_AttributeError, Py_TYPE, tp_name, tp_setattr, PyExc_RuntimeError

### 3.3.2. Type-specific Attribute Management

To keep things uncomplicated, we'll show only the char* version; the name parameter's type is all that separates the char* and [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* variants of the interface. In effect this example accomplishes what the generic example above does, yet it forgoes the generic support introduced in Python 2.2. It walks through how the handler functions get invoked, so that should you ever need to broaden their behavior, you'll grasp what has to happen.

Python calls the [`tp_getattr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_getattr) handler whenever an object needs an attribute looked up. It fires in the very circumstances where a class's [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) method would be triggered.

Here is an example:

```c
static PyObject *
newdatatype_getattr(PyObject *op, char *name)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    if (strcmp(name, "data") == 0) {
        return PyLong_FromLong(self->data);
    }

    PyErr_Format(PyExc_AttributeError,
                 "'%.100s' object has no attribute '%.400s'",
                 Py_TYPE(self)->tp_name, name);
    return NULL;
}

```

The [`tp_setattr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_setattr) handler fires whenever a class instance's [`__setattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setattr__) or [`__delattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delattr__) method would run. Whenever an attribute is meant to be removed, the third parameter arrives as `NULL`. The example below merely throws an exception; were that truly the whole of what you needed, you should instead set the `tp_setattr` handler to `NULL`.

```c
static int
newdatatype_setattr(PyObject *op, char *name, PyObject *v)
{
    PyErr_Format(PyExc_RuntimeError, "Read-only attribute: %s", name);
    return -1;
}

```

[Subject index](INDEX.md) · [Previous source section](generic-attribute-management-and-py-readonly.md) · [Next source section](object-comparison-and-py-newref.md)
