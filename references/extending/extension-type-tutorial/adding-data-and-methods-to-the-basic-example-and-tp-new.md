# Adding data and methods to the Basic example — PyObject_HEAD, PyObject, Custom_dealloc, Py_XDECREF, Py_TYPE, tp_free, tp_dealloc, PyTypeObject, tp_new

A handful of changes distinguish this revision of the module.

The C struct backing the `Custom` type now holds three data attributes, *first*, *last*, and *number*. As Python strings, *first* and *last* carry first and last names. Meanwhile *number* is stored as a C integer.

The object structure changes to match:

```c
typedef struct {
    PyObject_HEAD
    PyObject *first; /* first name */
    PyObject *last;  /* last name */
    int number;
} CustomObject;

```

Now that there’s data under management, allocation and deallocation of objects demand extra attention. At the very least, a deallocation method becomes necessary:

```c
static void
Custom_dealloc(PyObject *op)
{
    CustomObject *self = (CustomObject *) op;
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free(self);
}

```

which we wire into the [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) member:

```c
.tp_dealloc = Custom_dealloc,

```

To begin, this method drops the reference counts of the pair of Python attributes. The [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) function deals gracefully with a `NULL` argument (something that can arise here when `tp_new` bailed out partway through). After that it reaches for the [`tp_free`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_free) member belonging to the object’s type (obtained via `Py_TYPE(self)`) so the object’s memory is released. Bear in mind that the object’s type may differ from `CustomType`, since the object could be an instance of a subclass.

Note

We need the explicit cast to `CustomObject *` shown above because `Custom_dealloc` was written to accept a `PyObject *` argument, matching the `PyObject *` argument the `tp_dealloc` function pointer is meant to receive. Because we assign to a type’s `tp_dealloc` slot, we’re asserting that it will only ever run against instances of our `CustomObject` class, which makes the cast to `(CustomObject *)` safe. That’s object-oriented polymorphism — in C!

Within legacy code, or in older editions of this tutorial, you may run across comparable functions that accept a pointer to the subtype object structure (`CustomObject*`) outright, like this:

```c
Custom_dealloc(CustomObject *self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free((PyObject *) self);
}
...
.tp_dealloc = (destructor) Custom_dealloc,

```

On every architecture CPython runs on this behaves identically, yet under the rules of the C standard it triggers undefined behavior.

Because we want the first and last names set to empty strings from the start, we furnish a `tp_new` implementation:

[Subject index](INDEX.md) · [Previous source section](custom-type-methods-and-module-initialization.md) · [Next source section](adding-data-and-methods-to-the-basic-example-and-tp-base.md) · [Owning section and setup](adding-data-and-methods-to-the-basic-example.md)
