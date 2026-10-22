# traverseproc PyTypeObject.tp_traverse

[traverseproc](https://docs.python.org/3.14/c-api/gcsupport.html#c.traverseproc) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_traverse

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_traverse` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a traversal routine used by the garbage collector. It comes into play only when the `Py_TPFLAGS_HAVE_GC` flag bit is enabled. Here is the signature:

```c
int tp_traverse(PyObject *self, visitproc visit, void *arg);

```

You can read more about Python’s garbage collection design in the section [Supporting Cyclic Garbage Collection](https://docs.python.org/3.14/c-api/gcsupport.html#supporting-cycle-detection).

The garbage collector relies on the `tp_traverse` pointer to spot reference cycles. A common way to write a `tp_traverse` function is simply to invoke [`Py_VISIT()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.Py_VISIT) for each Python-object member the instance owns. As an example, here is the `local_traverse()` function taken from the `_thread` extension module:

```c
static int
local_traverse(PyObject *op, visitproc visit, void *arg)
{
    localobject *self = (localobject *) op;
    Py_VISIT(self->args);
    Py_VISIT(self->kw);
    Py_VISIT(self->dict);
    return 0;
}

```

Observe that [`Py_VISIT()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.Py_VISIT) is invoked only for members that could be involved in reference cycles. While a `self->key` member also exists, it is restricted to being either `NULL` or a Python string and so cannot take part in a reference cycle.

Conversely, even when you are certain a member can never belong to a cycle, you might choose to visit it regardless, as a debugging convenience, so that the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module’s [`get_referents()`](https://docs.python.org/3.14/library/gc.html#gc.get_referents) function reports it.

Heap types (`Py_TPFLAGS_HEAPTYPE`) are required to visit their type with:

```c
Py_VISIT(Py_TYPE(self));

```

This is required only from Python 3.9 onward. For compatibility with Python 3.8 and earlier, wrap the line in a condition:

```c
#if PY_VERSION_HEX >= 0x03090000
    Py_VISIT(Py_TYPE(self));
#endif

```

When the `Py_TPFLAGS_MANAGED_DICT` bit is enabled in the `tp_flags` field, the traverse function is required to invoke [`PyObject_VisitManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_VisitManagedDict) as follows:

```c
PyObject_VisitManagedDict((PyObject*)self, visit, arg);

```

Warning

While writing `tp_traverse`, you should visit only the members the instance actually *owns* (by holding [strong references](https://docs.python.org/3.14/glossary.html#term-strong-reference) to them). For example, when an object permits weak references through the `tp_weaklist` slot, the pointer backing the linked list (whatever *tp_weaklist* refers to) must **not** be visited, because the instance does not itself own the weak references pointing at it (the weakreference list exists to drive the weak reference machinery, yet the instance holds no strong reference to its contents, since they may be removed even while the instance lives on).

Warning

The traversal routine must be free of side effects. It may neither change the reference counts of any Python objects nor build or tear down any Python objects.

Keep in mind that [`Py_VISIT()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.Py_VISIT) insists that the *visit* and *arg* parameters of `local_traverse()` carry exactly those names; pick anything else and it breaks.

Heap-allocated type instances keep a reference to their type. Consequently, their traversal routine has to either visit [`Py_TYPE(self)`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) or hand that duty off by calling the `tp_traverse` of some other heap-allocated type (for instance, a heap-allocated superclass). Omitting this can leave the type object ineligible for garbage collection.

Note

Any thread may call the `tp_traverse` function.

Changed in version 3.9: Heap-allocated types must now visit `Py_TYPE(self)` within `tp_traverse`. With earlier Python releases, on account of [bug 40217](https://bugs.python.org/issue40217), doing so could trigger crashes in subclasses.

**Inheritance:**

Group: `Py_TPFLAGS_HAVE_GC`, `tp_traverse`, `tp_clear`

This field passes to subtypes alongside `tp_clear` and the `Py_TPFLAGS_HAVE_GC` flag bit: the base type contributes the flag bit, `tp_traverse`, and `tp_clear` together whenever all three are zero in the subtype.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](py-tpflags-sequence-to-pytypeobject-tp-doc.md) · [Following source contract](pytypeobject-tp-clear.md)
