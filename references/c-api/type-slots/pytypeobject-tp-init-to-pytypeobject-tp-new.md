# type slots C API: Type initialization and allocation slots

initproc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_init

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_init` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to an instance initialization function.

This function is the counterpart of the [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method on classes. As with `__init__()`, an instance can be created without `__init__()` running, and an instance can be reinitialized by invoking its `__init__()` method once more.

The function signature is:

```c
int tp_init(PyObject *self, PyObject *args, PyObject *kwds);

```

The self argument is the instance being initialized; the *args* and *kwds* arguments carry the positional and keyword arguments supplied to the call to [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__).

When non-`NULL`, the `tp_init` function runs as part of creating an instance in the usual way by calling its type, once the type’s `tp_new` function has produced an instance of the type. Should `tp_new` yield an instance of an unrelated type that is not a subtype of the original, no `tp_init` runs; should `tp_new` yield an instance of a subtype of the original, the subtype’s `tp_init` runs.

Returns `0` on success, `-1` and sets an exception on error.

**Inheritance:**

Subtypes inherit this field.

**Default:**

This field carries no default for static types.

 allocfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_alloc

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_alloc` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to an instance allocation function.

The function signature is:

```c
PyObject *tp_alloc(PyTypeObject *self, Py_ssize_t nitems);

```

**Inheritance:**

Static subtypes inherit this slot; when inherited from [`object`](https://docs.python.org/3.14/library/functions.html#object) it will be [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc).

This slot is not inherited by heap subtypes.

**Default:**

For heap subtypes, this field is invariably set to [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc).

For static subtypes, this slot is inherited (see above).

 newfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_new

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_new` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to an instance creation function.

The function signature is:

```c
PyObject *tp_new(PyTypeObject *subtype, PyObject *args, PyObject *kwds);

```

The *subtype* argument names the type of the object under construction; the *args* and *kwds* arguments carry the positional and keyword arguments handed to the type’s call. Be aware that *subtype* need not match the type whose `tp_new` function runs; it can be a subtype of that type (yet not an unrelated type).

The `tp_new` function ought to invoke `subtype->tp_alloc(subtype, nitems)` to reserve space for the object, then carry out only the minimum further initialization that is strictly required. Any initialization that may safely be skipped or run again belongs in the `tp_init` handler. As a useful guideline, immutable types should do all their initialization in `tp_new`, whereas mutable types should leave the bulk of initialization to `tp_init`.

Setting the `Py_TPFLAGS_DISALLOW_INSTANTIATION` flag prevents the type’s instances from being created in Python.

**Inheritance:**

Subtypes inherit this field, with the exception that static types whose `tp_base` is `NULL` or `&PyBaseObject_Type` do not inherit it.

**Default:**

For static types this field has no default. Consequently, defining the slot as `NULL` means the type cannot be called to produce new instances; presumably some alternative route exists for making instances, such as a factory function.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-descr-get-to-pytypeobject-tp-dictoffset.md) · [Following source contract](pytypeobject-tp-free-to-pytypeobject-tp-cache.md)
