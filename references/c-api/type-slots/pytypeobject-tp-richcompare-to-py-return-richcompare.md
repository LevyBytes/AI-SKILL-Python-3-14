# type slots C API: `Py_RETURN_RICHCOMPARE()`

```c
static int
local_clear(PyObject *op)
{
    localobject *self = (localobject *) op;
    Py_CLEAR(self->key);
    Py_CLEAR(self->args);
    Py_CLEAR(self->kw);
    Py_CLEAR(self->dict);
    return 0;
}

```

Reach for the [`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR) macro, since clearing references is a delicate operation: the reference to the contained object must not be dropped (through [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF)) until the pointer to that contained object has first been set to `NULL`. The reason is that dropping the reference can turn the contained object into trash, kicking off a cascade of reclamation that may run arbitrary Python code (via finalizers, or weakref callbacks, tied to the contained object). Should such code be able to reach *self* once more, the pointer to the contained object needs to be `NULL` by then, so that *self* recognizes the contained object as no longer usable. The `Py_CLEAR()` macro carries out the steps in a safe sequence.

When the `Py_TPFLAGS_MANAGED_DICT` bit is enabled in the `tp_flags` field, the clear function is required to invoke [`PyObject_ClearManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_ClearManagedDict) as follows:

```c
PyObject_ClearManagedDict((PyObject*)self);

```

You can read more about Python’s garbage collection design in the section [Supporting Cyclic Garbage Collection](https://docs.python.org/3.14/c-api/gcsupport.html#supporting-cycle-detection).

**Inheritance:**

Group: `Py_TPFLAGS_HAVE_GC`, `tp_traverse`, `tp_clear`

This field passes to subtypes alongside `tp_traverse` and the `Py_TPFLAGS_HAVE_GC` flag bit: the base type contributes the flag bit, `tp_traverse`, and `tp_clear` together whenever all three are zero in the subtype.

See also

[Object Life Cycle](https://docs.python.org/3.14/c-api/lifecycle.html#life-cycle) for the details of how this slot connects to the others.

 richcmpfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_richcompare

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_richcompare` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to the rich comparison function, with this signature:

```c
PyObject *tp_richcompare(PyObject *self, PyObject *other, int op);

```

The first argument is guaranteed to be an instance of the type defined by [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).

The function ought to hand back the comparison result (typically `Py_True` or `Py_False`). When the comparison has no defined meaning, it must hand back `Py_NotImplemented`; when some other error arises, it must hand back `NULL` and raise an exception condition.

These constants are provided for use as the third argument to `tp_richcompare` and to [`PyObject_RichCompare()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompare):

| Constant | Comparison |
| --- | --- |
| Py_LT | `<` |
| Py_LE | `<=` |
| Py_EQ | `==` |
| Py_NE | `!=` |
| Py_GT | `>` |
| Py_GE | `>=` |

To make writing rich comparison functions easier, the following macro is provided:

 Py_RETURN_RICHCOMPARE(VAL_A, VAL_B, op)

Hand back `Py_True` or `Py_False` from the function according to how a comparison turns out. VAL_A and VAL_B have to be orderable through C comparison operators (they could, for instance, be C ints or floats). The third argument names the operation being requested, just as with [`PyObject_RichCompare()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompare).

What gets returned is a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference).

When an error occurs, it raises an exception and hands back `NULL` from the function.

Added in version 3.7.

**Inheritance:**

Group: `tp_hash`, `tp_richcompare`

This field passes to subtypes in tandem with `tp_hash`: a subtype takes on `tp_richcompare` and `tp_hash` whenever both the subtype’s `tp_richcompare` and `tp_hash` are `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) supplies a `tp_richcompare` implementation that may be inherited. Yet when only `tp_hash` is defined, not even that inherited function is applied, and instances of the type will be unable to take part in any comparisons.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [API declaration, ownership, ABI and error contract](pytypeobject-tp-clear.md) · [Following source contract](pytypeobject-tp-weaklistoffset-to-pytypeobject-tp-iternext.md)
