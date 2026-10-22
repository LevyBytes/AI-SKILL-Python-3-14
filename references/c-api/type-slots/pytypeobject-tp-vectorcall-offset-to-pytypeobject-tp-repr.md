# type slots C API: `PyTypeObject.tp_vectorcall_offset`, `PyTypeObject.tp_as_async`

[Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_vectorcall_offset

An optional offset pointing to a per-instance function that handles calling the object through the [vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall), a faster substitute for the more basic `tp_call`.

This field comes into play only when the `Py_TPFLAGS_HAVE_VECTORCALL` flag is enabled. When it is, the field must be a positive integer giving the offset, within the instance, of a [`vectorcallfunc`](https://docs.python.org/3.14/c-api/call.html#c.vectorcallfunc) pointer.

That *vectorcallfunc* pointer is allowed to be `NULL`, and when it is, the instance acts just as though `Py_TPFLAGS_HAVE_VECTORCALL` had not been enabled: calls to the instance revert to `tp_call`.

Every class that enables `Py_TPFLAGS_HAVE_VECTORCALL` is also required to set `tp_call` and to keep its behavior in line with the *vectorcallfunc* function. One way to achieve this is to point *tp_call* at [`PyVectorcall_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_Call).

Changed in version 3.8: Prior to version 3.8, this slot went by the name `tp_print`. Under Python 2.x it served to print to a file, while in Python 3.0 through 3.7 it went unused.

Changed in version 3.12: Up until version 3.12, mutable heap types were discouraged from implementing the vectorcall protocol. If a user assigns [`__call__`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) from Python code, only *tp_call* gets updated, which likely leaves it out of sync with the vectorcall function. As of 3.12, assigning `__call__` turns off the vectorcall optimization by clearing the `Py_TPFLAGS_HAVE_VECTORCALL` flag.

**Inheritance:**

This field is invariably inherited. The `Py_TPFLAGS_HAVE_VECTORCALL` flag, on the other hand, is not invariably inherited; should it remain unset, the subclass will not employ [vectorcall](https://docs.python.org/3.14/c-api/call.html#vectorcall) unless [`PyVectorcall_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_Call) is invoked directly.

 getattrfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_getattr

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_getattr` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to the get-attribute-string function.

This field has been deprecated. Where it is supplied, it should reference a function that behaves identically to the `tp_getattro` function, except that it accepts a C string rather than a Python string object for the attribute name.

**Inheritance:**

Group: `tp_getattr`, `tp_getattro`

A subtype inherits this field along with `tp_getattro`: a subtype picks up both `tp_getattr` and `tp_getattro` from its base type whenever the subtype's own `tp_getattr` and `tp_getattro` are each `NULL`.

 setattrfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_setattr

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_setattr` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to the function for setting and deleting attributes.

This field has been deprecated. Where it is supplied, it should reference a function that behaves identically to the `tp_setattro` function, except that it accepts a C string rather than a Python string object for the attribute name.

**Inheritance:**

Group: `tp_setattr`, `tp_setattro`

A subtype inherits this field along with `tp_setattro`: a subtype picks up both `tp_setattr` and `tp_setattro` from its base type whenever the subtype's own `tp_setattr` and `tp_setattro` are each `NULL`.

 PyAsyncMethods *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_as_async

Pointer to a supplementary structure holding fields that matter only for objects implementing the [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) and [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) protocols at the C level. Refer to Async Object Structures for the specifics.

Added in version 3.5: Formerly known as `tp_compare` and `tp_reserved`.

**Inheritance:**

The `tp_as_async` field is not inherited, but the contained fields are inherited individually.

 reprfunc [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_repr

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_repr` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a function that implements the built-in function [`repr()`](https://docs.python.org/3.14/library/functions.html#repr).

The signature is the same as for [`PyObject_Repr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Repr):

```c
PyObject *tp_repr(PyObject *self);

```

A string or Unicode object must be returned by the function. Ideally what it returns is a string that, once handed to [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) in an appropriate environment, yields an object equal in value. When that isn't practical, it should produce a string beginning with `'<'` and ending with `'>'` that conveys both the object's type and its value.

**Inheritance:**

This field is inherited by subtypes.

**Default:**

If this field goes unset, a string shaped like `<%s object at %p>` is produced, in which `%s` stands in for the type name and `%p` for the object's memory address.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](destructor-pytypeobject-tp-dealloc.md) · [Following source contract](pytypeobject-tp-as-number-to-pytypeobject-tp-call.md)
