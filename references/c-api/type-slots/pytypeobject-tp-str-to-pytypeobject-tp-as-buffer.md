# type slots C API: `PyTypeObject.tp_as_buffer`

reprfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_str

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_str` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a function that implements the built-in operation [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str). (Bear in mind that [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) is now a type, and `str()` invokes that type's constructor. That constructor in turn calls [`PyObject_Str()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Str) to perform the real work, and `PyObject_Str()` then dispatches to this handler.)

The signature is the same as for [`PyObject_Str()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Str):

```c
PyObject *tp_str(PyObject *self);

```

A string or Unicode object must be returned by the function. The result should be a "friendly" textual rendering of the object, since this is the rendering that, among other uses, the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function will rely on.

**Inheritance:**

This field is inherited by subtypes.

**Default:**

If this field is unset, [`PyObject_Repr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Repr) is invoked to produce a string representation.

 getattrofunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_getattro

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_getattro` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to the get-attribute function.

The signature is the same as for [`PyObject_GetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttr):

```c
PyObject *tp_getattro(PyObject *self, PyObject *attr);

```

A common convenience is to assign this field [`PyObject_GenericGetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericGetAttr), which carries out the standard procedure for locating object attributes.

**Inheritance:**

Group: `tp_getattr`, `tp_getattro`

A subtype inherits this field along with `tp_getattr`: a subtype picks up both `tp_getattr` and `tp_getattro` from its base type whenever the subtype's own `tp_getattr` and `tp_getattro` are each `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) uses [`PyObject_GenericGetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericGetAttr).

 setattrofunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_setattro

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_setattro` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to the function for setting and deleting attributes.

The signature is the same as for [`PyObject_SetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_SetAttr):

```c
int tp_setattro(PyObject *self, PyObject *attr, PyObject *value);

```

Beyond that, deleting an attribute by passing *value* as `NULL` has to be supported. A common convenience is to assign this field [`PyObject_GenericSetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericSetAttr), which carries out the standard procedure for assigning object attributes.

**Inheritance:**

Group: `tp_setattr`, `tp_setattro`

A subtype inherits this field along with `tp_setattr`: a subtype picks up both `tp_setattr` and `tp_setattro` from its base type whenever the subtype's own `tp_setattr` and `tp_setattro` are each `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) uses [`PyObject_GenericSetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericSetAttr).

 PyBufferProcs *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_as_buffer

Pointer to a supplementary structure holding fields that matter only for objects implementing the buffer interface. Documentation for these fields appears in Buffer Object Structures.

**Inheritance:**

The `tp_as_buffer` field is not inherited, but the contained fields are inherited individually.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-as-number-to-pytypeobject-tp-call.md) · [Following source contract](pytypeobject-tp-flags-to-py-tpflags-default.md)
