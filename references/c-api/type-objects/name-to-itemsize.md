# type objects C API: Type-specification name and instance-size fields

const char *name

The type's name, applied to populate [`PyTypeObject.tp_name`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_name).

 int basicsize

A positive value gives the instance's byte size and feeds into [`PyTypeObject.tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize).

A value of zero signals that [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) ought to be inherited.

When negative, the magnitude tells how much room the class's instances require *in addition* to what the superclass uses. Reach for [`PyObject_GetTypeData()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetTypeData) to obtain a pointer into the subclass-specific memory set aside this way. Where `basicsize` is negative, Python adds padding as required so that [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize)’s alignment is satisfied.

Changed in version 3.12: In earlier releases a negative value here was not allowed.

 int itemsize

The byte size of a single element within a variable-size type. It populates [`PyTypeObject.tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize). Consult the `tp_itemsize` documentation for the caveats.

A zero here causes [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize) to be inherited. Subclassing arbitrary variable-sized classes carries risk, because certain types place variable-sized memory at a fixed offset that can then collide with fixed-sized memory a subclass relies on. As a safeguard against such errors, `itemsize` may be inherited only under these circumstances:

- The base happens not to be variable-sized (its [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize)).

- A positive `PyType_Spec.basicsize` was asked for, which implies the base class's memory layout is understood.

- A `PyType_Spec.basicsize` of zero was asked for, which implies the subclass never reaches the instance’s memory directly.

- When the [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END) flag is present.

 unsigned int flags

The type flags, applied to populate [`PyTypeObject.tp_flags`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_flags).

Whenever the `Py_TPFLAGS_HEAPTYPE` flag is absent, `PyType_FromSpecWithBases()` turns it on for you.

 PyType_Slot *slots

An array made of `PyType_Slot` structures. The special slot value `{0, NULL}` marks its end.

No slot ID ought to appear more than a single time.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytype-frommetaclass-to-pytype-fromspec.md) · [Owning structure and shared ABI conditions](pytype-spec.md) · [Following source contract](pytype-slot-to-py-tp-doc.md)
