# type slots C API: `PyObject_CallFinalizerFromDealloc()`, `PyTypeObject.tp_watched`

[`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3.14/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc)

 [vectorcallfunc](https://docs.python.org/3.14/c-api/call.html#c.vectorcallfunc) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_vectorcall

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_vectorcall` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

A [vectorcall function](https://docs.python.org/3.14/c-api/call.html#vectorcall) applied to calls made on the type object itself (as opposed to its instances). Put differently, `tp_vectorcall` serves to speed up `type.__call__`, which generally yields a fresh instance of *type*.

Like every vectorcall function, when `tp_vectorcall` is `NULL`, the *tp_call* protocol (`Py_TYPE(type)->tp_call`) takes over instead.

Note

Under the [vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall), the vectorcall function is required to behave identically to the matching `tp_call`. Consequently, `type->tp_vectorcall` is obliged to mirror the behavior of `Py_TYPE(type)->tp_call`.

In particular, when *type* relies on the default metaclass, `type->tp_vectorcall` is required to act the same as [PyType_Type](https://docs.python.org/3.14/c-api/type.html#c.PyType_Type)->tp_call, which:

- calls `type->tp_new`,

- when what comes back is a subclass of *type*, applies `type->tp_init` to that `tp_new` output, and

- returns the result of `tp_new`.

Generally, `tp_vectorcall` gets overridden so as to streamline this sequence for particular `tp_new` and `tp_init`. While applying this to user-subclassable types, bear in mind that each of them may be overridden (through [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) and [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__), respectively).

**Inheritance:**

Subtypes never inherit this field.

Added in version 3.9: (although present from 3.8 onward, the field only sees use beginning with 3.9)

 unsigned char [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_watched

Internal. Do not use.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pyobject-callfinalizer.md) · [Following source contract](static-types.md)
