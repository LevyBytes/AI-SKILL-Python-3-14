# type slots C API: `PyTypeObject.tp_flags`, `Py_TPFLAGS_HEAPTYPE`, `Py_TPFLAGS_BASETYPE`, `Py_TPFLAGS_READY`, `Py_TPFLAGS_READYING`, `Py_TPFLAGS_HAVE_GC`, `Py_TPFLAGS_DEFAULT`

unsigned long [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_flags

This field holds a bit mask made up of assorted flags. Certain flags signal alternate semantics for particular cases; others serve to mark that specific fields in the type object (or in the extension structures reached through `tp_as_number`, `tp_as_sequence`, `tp_as_mapping`, and `tp_as_buffer`), which historically were not always present, are valid; whenever such a flag bit is clear, the fields it protects must not be touched and are to be treated as holding a zero or `NULL` value instead.

**Inheritance:**

How this field is inherited is intricate. The bulk of flag bits are inherited one at a time, so that when the base type has a flag bit set, the subtype inherits that flag bit. Flag bits tied to extension structures are inherited strictly along with the extension structure itself; that is, the value of the flag bit on the base type gets duplicated into the subtype alongside a pointer pointing at the extension structure. As for the `Py_TPFLAGS_HAVE_GC` flag bit, it travels with the `tp_traverse` and `tp_clear` fields — so it is inherited if the `Py_TPFLAGS_HAVE_GC` flag bit is clear on the subtype while the subtype's `tp_traverse` and `tp_clear` fields are present and hold `NULL` values.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) uses `Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE`.

**Bit Masks:**

The bit masks listed below are the ones presently defined; you can combine them with the `|` operator to build the value placed in the `tp_flags` field. The macro [`PyType_HasFeature()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_HasFeature) accepts a type and a flags value, *tp* and *f*, and tests whether `tp->tp_flags & f` comes out non-zero.

 Py_TPFLAGS_HEAPTYPE

This bit becomes set when the type object itself lives on the heap — for instance, types built at runtime via [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec). Under those circumstances the [`ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type) field of the type's instances counts as a reference to the type, so the type object is INCREF'ed whenever a fresh instance is made and DECREF'ed whenever an instance is destroyed (this excludes instances of subtypes; only the type that the instance's ob_type points at gets INCREF'ed or DECREF'ed). Heap types ought to additionally [support garbage collection](https://docs.python.org/3.14/c-api/gcsupport.html#supporting-cycle-detection), since they may create a reference cycle together with their own module object.

**Inheritance:**

The upstream reference does not specify inheritance for this flag.

 Py_TPFLAGS_BASETYPE

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This bit becomes set when the type is allowed to serve as the base type for another type. When this bit is clear, the type cannot be subtyped (akin to a "final" class in Java).

**Inheritance:**

The upstream reference does not specify inheritance for this flag.

 Py_TPFLAGS_READY

This bit becomes set once the type object has been completely initialized by [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready).

**Inheritance:**

The upstream reference does not specify inheritance for this flag.

 Py_TPFLAGS_READYING

This bit stays set while [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) is busy initializing the type object.

**Inheritance:**

The upstream reference does not specify inheritance for this flag.

 Py_TPFLAGS_HAVE_GC

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This bit becomes set when the object supports garbage collection. With this bit set, memory for new instances (refer to `tp_alloc`) has to be allocated through [`PyObject_GC_New`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_New) or [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc) and freed (refer to `tp_free`) through [`PyObject_GC_Del()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_GC_Del). Further details appear in the section [Supporting Cyclic Garbage Collection](https://docs.python.org/3.14/c-api/gcsupport.html#supporting-cycle-detection).

**Inheritance:**

Group: `Py_TPFLAGS_HAVE_GC`, `tp_traverse`, `tp_clear`

The `Py_TPFLAGS_HAVE_GC` flag bit travels alongside the `tp_traverse` and `tp_clear` fields when inherited — meaning it is inherited when the `Py_TPFLAGS_HAVE_GC` flag bit is clear on the subtype while the subtype's `tp_traverse` and `tp_clear` fields are present and hold `NULL` values.

 Py_TPFLAGS_DEFAULT

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is a bitmask covering every bit that concerns whether certain fields exist in the type object and its extension structures. At present it comprises the following bits: `Py_TPFLAGS_HAVE_STACKLESS_EXTENSION`.

**Inheritance:**

The upstream reference does not specify inheritance for this flag.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-str-to-pytypeobject-tp-as-buffer.md) · [Following source contract](py-tpflags-method-descriptor-to-py-tpflags-items-at-end.md)
