# type slots C API: `PyTypeObject.tp_as_number`, `PyTypeObject.tp_as_sequence`, `PyTypeObject.tp_as_mapping`

PyNumberMethods *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_as_number

Pointer to a supplementary structure holding fields that matter only for objects implementing the number protocol. Documentation for these fields appears in Number Object Structures.

**Inheritance:**

The `tp_as_number` field is not inherited, but the contained fields are inherited individually.

 PySequenceMethods *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_as_sequence

Pointer to a supplementary structure holding fields that matter only for objects implementing the sequence protocol. Documentation for these fields appears in Sequence Object Structures.

**Inheritance:**

The `tp_as_sequence` field is not inherited, but the contained fields are inherited individually.

 PyMappingMethods *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_as_mapping

Pointer to a supplementary structure holding fields that matter only for objects implementing the mapping protocol. Documentation for these fields appears in Mapping Object Structures.

**Inheritance:**

The `tp_as_mapping` field is not inherited, but the contained fields are inherited individually.

 hashfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_hash

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_hash` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a function that implements the built-in function [`hash()`](https://docs.python.org/3.14/library/functions.html#hash).

The signature is the same as for [`PyObject_Hash()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Hash):

```c
Py_hash_t tp_hash(PyObject *);

```

The value `-1` ought not to be handed back as an ordinary result; should an error arise while the hash value is being computed, the function is expected to set an exception and return `-1`.

If this field goes unset (*and* `tp_richcompare` is likewise unset), trying to compute the object's hash triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). The effect matches assigning it [`PyObject_HashNotImplemented()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HashNotImplemented).

You can deliberately assign this field [`PyObject_HashNotImplemented()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HashNotImplemented) to prevent the hash method from being inherited out of a parent type. At the Python level this reads as the same thing as `__hash__ = None`, which makes `isinstance(o, collections.Hashable)` properly yield `False`. Bear in mind the reverse holds as well — assigning `__hash__ = None` to a class from Python causes the `tp_hash` slot to be set to `PyObject_HashNotImplemented()`.

**Inheritance:**

Group: `tp_hash`, `tp_richcompare`

A subtype inherits this field along with `tp_richcompare`: a subtype picks up both `tp_richcompare` and `tp_hash` whenever the subtype's own `tp_richcompare` and `tp_hash` are each `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) uses [`PyObject_GenericHash()`](https://docs.python.org/3.14/c-api/hash.html#c.PyObject_GenericHash).

 ternaryfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_call

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_call` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a routine that carries out invocation of the object. Keep this at `NULL` when the object cannot be called. The signature matches that of [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call):

```c
PyObject *tp_call(PyObject *self, PyObject *args, PyObject *kwargs);

```

**Inheritance:**

This field is inherited by subtypes.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-vectorcall-offset-to-pytypeobject-tp-repr.md) · [Following source contract](pytypeobject-tp-str-to-pytypeobject-tp-as-buffer.md)
