# type slots C API: `PyTypeObject.tp_bases`, `PyTypeObject.tp_mro`, `PyTypeObject.tp_cache`

freefunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_free

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_free` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to an instance deallocation function. Its signature is:

```c
void tp_free(void *self);

```

The job of this function is to release the memory that `tp_alloc` reserved.

**Inheritance:**

Static subtypes inherit this slot; when inherited from [`object`](https://docs.python.org/3.14/library/functions.html#object) it will be [`PyObject_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Free). One exception applies: when the type supports garbage collection (that is, `tp_flags` has the `Py_TPFLAGS_HAVE_GC` flag set) and would have inherited `PyObject_Free()`, the slot is not inherited and instead falls back to [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del).

This slot is not inherited by heap subtypes.

**Default:**

For heap subtypes, this slot defaults to a deallocator chosen to pair with [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) and the setting of the `Py_TPFLAGS_HAVE_GC` flag.

For static subtypes, this slot is inherited (see above).

 [inquiry](https://docs.python.org/3.14/c-api/gcsupport.html#c.inquiry) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_is_gc

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_is_gc` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a function that the garbage collector invokes.

The garbage collector has to determine whether a given object can be collected. Usually it is enough to inspect the `tp_flags` field of the object’s type and test the `Py_TPFLAGS_HAVE_GC` flag bit. Yet certain types hold a blend of statically and dynamically allocated instances, and the statically allocated ones cannot be collected. Types like that should supply this function; it should return `1` for an instance that is collectible and `0` for one that is not. The signature is:

```c
int tp_is_gc(PyObject *self);

```

(Types themselves are the sole example of this. The metatype, [`PyType_Type`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Type), defines this function so it can tell statically allocated types apart from dynamically allocated ones.)

**Inheritance:**

Subtypes inherit this field.

**Default:**

There is no default for this slot. When this field is `NULL`, `Py_TPFLAGS_HAVE_GC` serves as the functional equivalent.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_bases

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_bases` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Tuple of base types.

Set this field to `NULL` and treat it as read-only. Python populates it once the type is [`initialized`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready).

When classes are created dynamically, the `Py_tp_bases` [`slot`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) may stand in for the *bases* argument of [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases). The argument form is preferred.

Warning

Statically defined types do not handle multiple inheritance gracefully. Assigning a tuple to `tp_bases` will not make Python raise an error, but certain slots will be inherited only from the first base.

**Inheritance:**

This field is not inherited.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_mro

Tuple holding the fully expanded collection of base types, beginning with the type itself and finishing with [`object`](https://docs.python.org/3.14/library/functions.html#object), in Method Resolution Order.

Set this field to `NULL` and treat it as read-only. Python populates it once the type is [`initialized`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready).

**Inheritance:**

This field is not inherited; [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) recomputes it from scratch.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_cache

Unused. Internal use only.

**Inheritance:**

This field is not inherited.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-init-to-pytypeobject-tp-new.md) · [Following source contract](pytypeobject-tp-subclasses-to-pytypeobject-tp-version-tag.md)
