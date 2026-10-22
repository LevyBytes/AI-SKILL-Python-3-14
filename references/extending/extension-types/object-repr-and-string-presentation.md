# Object Presentation — tp_repr, tp_str, PyTypeObject, PyObject, PyUnicode_FromFormat, tp_name

### 3.2. Object Presentation

Two mechanisms exist in Python for producing a textual rendering of an object: the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function and the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) function. (As for [`print()`](https://docs.python.org/3.14/library/functions.html#print), it merely calls `str()`.) Neither of these handlers is required.

```c
reprfunc tp_repr;
reprfunc tp_str;

```

What the [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) handler ought to do is hand back a string object holding a representation of whichever instance triggered it. A straightforward example follows:

```c
static PyObject *
newdatatype_repr(PyObject *op)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    return PyUnicode_FromFormat("Repr-ified_newdatatype{{size:%d}}",
                                self->obj_UnderlyingDatatypePtr->size);
}

```

Without a [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) handler in place, the interpreter falls back on a representation built from the type's [`tp_name`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_name) plus a value that identifies the object uniquely.

For [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str), the [`tp_str`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_str) handler plays the same role that the [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) handler covered above plays for [`repr()`](https://docs.python.org/3.14/library/functions.html#repr); in other words, Python invokes it whenever code runs `str()` against one of your object's instances. Its implementation closely mirrors the `tp_repr` function, except the string it yields is meant to be read by people. When `tp_str` is left out, the `tp_repr` handler stands in for it.

A straightforward example follows:

```c
static PyObject *
newdatatype_str(PyObject *op)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    return PyUnicode_FromFormat("Stringified_newdatatype{{size:%d}}",
                                self->obj_UnderlyingDatatypePtr->size);
}

```

[Subject index](INDEX.md) · [Previous source section](finalization-and-de-allocation-and-tp-finalize.md) · [Next source section](attribute-access-slots.md)
