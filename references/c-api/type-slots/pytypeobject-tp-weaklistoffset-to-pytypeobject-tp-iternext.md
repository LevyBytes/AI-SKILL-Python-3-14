# type slots C API: `PyTypeObject.tp_weaklistoffset`

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_weaklistoffset

Although this field remains supported, prefer `Py_TPFLAGS_MANAGED_WEAKREF` whenever you possibly can.

When instances of this type can be weakly referenced, this field is positive and holds the offset, within the instance structure, of the head of the weak reference list (disregarding the GC header should one exist); [`PyObject_ClearWeakRefs()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyObject_ClearWeakRefs) and the `PyWeakref_*` functions rely on this offset. The instance structure has to contain a field of type [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* initialized to `NULL`.

Take care not to mix this field up with `tp_weaklist`; the latter is the list head for weak references aimed at the type object itself.

Enabling both the `Py_TPFLAGS_MANAGED_WEAKREF` bit and `tp_weaklistoffset` is an error.

**Inheritance:**

Subtypes inherit this field, though note the rules given below. A subtype is free to override the offset; that simply means the subtype relies on a weak reference list head distinct from the base type’s. Because the list head is always located through `tp_weaklistoffset`, this poses no problem.

**Default:**

When the `Py_TPFLAGS_MANAGED_WEAKREF` bit is enabled in the `tp_flags` field, `tp_weaklistoffset` is assigned a negative value, signaling that relying on this field is unsafe.

 getiterfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_iter

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_iter` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a function returning an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) for the object. Having it usually indicates that instances of this type are [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) (though sequences can be iterable even without this function).

This function carries the same signature as [`PyObject_GetIter()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetIter):

```c
PyObject *tp_iter(PyObject *self);

```

**Inheritance:**

Subtypes inherit this field.

 iternextfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_iternext

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_iternext` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a function returning the following item from an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). Its signature is:

```c
PyObject *tp_iternext(PyObject *self);

```

Once the iterator runs out, it must return `NULL`; a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception may or may not be set. If a different error arises, it likewise must return `NULL`. Having it indicates that instances of this type are iterators.

Iterator types ought to define the `tp_iter` function as well, and that function should hand back the iterator instance itself (rather than a fresh iterator instance).

This function carries the same signature as [`PyIter_Next()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Next).

**Inheritance:**

Subtypes inherit this field.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-richcompare-to-py-return-richcompare.md)
