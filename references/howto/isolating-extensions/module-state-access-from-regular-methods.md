# Module State Access from Regular Methods

### Module State Access from Regular Methods

Reaching the module-level state from the methods of a class is a little trickier, yet doable owing to API added in Python 3.9. To obtain the state, you must first obtain the *defining class*, then derive the module state from it.

The biggest obstacle is fetching *the class a method was defined in*, or for short that method's ?defining class?. The defining class is able to carry a reference to the module it belongs to.

Take care not to mix up the defining class with `Py_TYPE(self)`. When the method is invoked on a *subclass* of your type, `Py_TYPE(self)` will point at that subclass, which might live in a different module than yours.

Note

The Python code below can demonstrate the idea. `Base.get_defining_class` yields `Base` even where `type(self) == Sub`:

```python
class Base:
    def get_type_of_self(self):
        return type(self)

    def get_defining_class(self):
        return __class__

class Sub(Base):
    pass

```

For a method to obtain its ?defining class?, it has to adopt the [METH_METHOD | METH_FASTCALL | METH_KEYWORDS](https://docs.python.org/3.14/c-api/structures.html#meth-method-meth-fastcall-meth-keywords) [`calling convention`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) plus the matching [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod) signature:

```c
PyObject *PyCMethod(
    PyObject *self,               // object the method was called on
    PyTypeObject *defining_class, // defining class
    PyObject *const *args,        // C array of arguments
    Py_ssize_t nargs,             // length of "args"
    PyObject *kwnames)            // NULL, or dict of keyword arguments

```

After you hold the defining class, invoke [`PyType_GetModuleState()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleState) to obtain the state of its linked module.

For instance:

```c
static PyObject *
example_method(PyObject *self,
        PyTypeObject *defining_class,
        PyObject *const *args,
        Py_ssize_t nargs,
        PyObject *kwnames)
{
    my_struct *state = (my_struct*)PyType_GetModuleState(defining_class);
    if (state == NULL) {
        return NULL;
    }
    ... // rest of logic
}

PyDoc_STRVAR(example_method_doc, "...");

static PyMethodDef my_methods[] = {
    {"example_method",
      (PyCFunction)(void(*)(void))example_method,
      METH_METHOD|METH_FASTCALL|METH_KEYWORDS,
      example_method_doc}
    {NULL},
}

```

[Subject index](INDEX.md) · [Previous source context](module-state-access-from-classes.md) · [Following source context](module-state-access-from-slot-methods-getters-and-setters.md)
