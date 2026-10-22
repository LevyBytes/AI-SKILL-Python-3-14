# Adding data and methods to the Basic example — PyObject, Custom_new, PyTypeObject, tp_alloc, PyUnicode_FromString, Py_DECREF, tp_new, PyType_GenericNew, tp_init, PyType_Ready, tp_base

```c
static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    CustomObject *self;
    self = (CustomObject *) type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->last = PyUnicode_FromString("");
        if (self->last == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }
    return (PyObject *) self;
}

```

and we slot it into the [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) member:

```c
.tp_new = Custom_new,

```

It’s the `tp_new` handler’s job to create objects of the type, as distinct from initializing them. Within Python it shows up as the [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method. Defining a `tp_new` member isn’t obligatory, and many extension types do indeed just lean on [`PyType_GenericNew()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericNew), exactly as the first version of the `Custom` type did above. Here, though, we put the `tp_new` handler to work initializing the `first` and `last` attributes to non-`NULL` defaults.

Into `tp_new` come the type being instantiated (which need not be `CustomType`, when a subclass is the one being instantiated) together with whatever arguments accompanied the call to the type, and it is supposed to hand back the instance it built. While `tp_new` handlers always take positional and keyword arguments, they frequently disregard them, deferring the argument processing to initializer methods (otherwise known as `tp_init` in C or `__init__` in Python).

Note

`tp_new` should refrain from invoking `tp_init` on its own, because the interpreter takes care of that itself.

To grab memory, the `tp_new` implementation calls into the [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot:

```c
self = (CustomObject *) type->tp_alloc(type, 0);

```

Given that memory allocation can fail, we’re obliged to test the [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) result against `NULL` before moving on.

Note

We never populated the [`tp_alloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_alloc) slot ourselves. Instead [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) sets it for us, inheriting it from our base class, which defaults to [`object`](https://docs.python.org/3.14/library/functions.html#object). The default allocation scheme suits most types.

Note

When you build a co-operative [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) (one that chains to a base type’s `tp_new` or [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__)), you must *not* attempt to figure out which method to invoke by consulting the method resolution order at runtime. Decide statically which type you intend to call and invoke its `tp_new` directly, or go through `type->tp_base->tp_new`. Neglecting this can break Python subclasses of your type that additionally inherit from other Python-defined classes. (More precisely, you might find it impossible to make instances of those subclasses without running into a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).)

We also write an initialization function that takes arguments to supply starting values for our instance:

[Subject index](INDEX.md) · [Previous source section](adding-data-and-methods-to-the-basic-example-and-tp-new.md) · [Next source section](adding-data-and-methods-to-the-basic-example-and-tp-members.md) · [Owning section and setup](adding-data-and-methods-to-the-basic-example.md)
