# type slots C API: `PyTypeObject.tp_dictoffset`

descrgetfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_descr_get

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_descr_get` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a “descriptor get” function.

The function signature is:

```c
PyObject * tp_descr_get(PyObject *self, PyObject *obj, PyObject *type);

```

**Inheritance:**

Subtypes inherit this field.

 descrsetfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_descr_set

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_descr_set` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a function that sets and deletes a descriptor’s value.

The function signature is:

```c
int tp_descr_set(PyObject *self, PyObject *obj, PyObject *value);

```

Passing `NULL` for the *value* argument deletes the value.

**Inheritance:**

Subtypes inherit this field.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_dictoffset

This field remains supported, but wherever feasible you should prefer `Py_TPFLAGS_MANAGED_DICT` in its place.

When instances of this type carry a dictionary of instance variables, this field is non-zero and stores the offset, within the type’s instances, of the instance variable dictionary; [`PyObject_GenericGetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericGetAttr) relies on that offset.

Take care not to mix up this field with `tp_dict`; the latter is the dictionary holding attributes of the type object itself.

The value gives the dictionary’s offset measured from the beginning of the instance structure.

Treat `tp_dictoffset` as write-only. Obtain the dictionary pointer by calling [`PyObject_GenericGetDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GenericGetDict). Since `PyObject_GenericGetDict()` might have to allocate memory for the dictionary, calling [`PyObject_GetAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetAttr) to read an attribute on the object may be more efficient.

Setting both the `Py_TPFLAGS_MANAGED_DICT` bit and `tp_dictoffset` is an error.

**Inheritance:**

Subtypes inherit this field. A subtype ought not to override this offset; overriding it can be unsafe should C code attempt to reach the dictionary at the earlier offset. For correct inheritance support, use `Py_TPFLAGS_MANAGED_DICT`.

**Default:**

There is no default for this slot. With static types, a `NULL` field means no [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) is produced for instances.

When the `tp_flags` field has the `Py_TPFLAGS_MANAGED_DICT` bit set, `tp_dictoffset` will be assigned `-1`, signaling that using this field is unsafe.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-methods-to-pytypeobject-tp-dict.md) · [Following source contract](pytypeobject-tp-init-to-pytypeobject-tp-new.md)
