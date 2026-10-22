# type slots C API: `Py_TPFLAGS_METHOD_DESCRIPTOR`, `Py_TPFLAGS_MANAGED_DICT`, `Py_TPFLAGS_MANAGED_WEAKREF`, `Py_TPFLAGS_ITEMS_AT_END`

Py_TPFLAGS_METHOD_DESCRIPTOR

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

This bit signals that objects behave like unbound methods.

When this flag is set for `type(meth)`, then:

- `meth.__get__(obj, cls)(*args, **kwds)` (with `obj` not None) must be equivalent to `meth(obj, *args, **kwds)`.

- `meth.__get__(None, cls)(*args, **kwds)` must be equivalent to `meth(*args, **kwds)`.

This flag unlocks an optimization for everyday method calls such as `obj.meth()`: it sidesteps building a throwaway "bound method" object for `obj.meth`.

Added in version 3.8.

**Inheritance:**

Types lacking the `Py_TPFLAGS_IMMUTABLETYPE` flag never inherit this flag. Where extension types are concerned, it carries over each time `tp_descr_get` carries over.

 Py_TPFLAGS_MANAGED_DICT

This bit signals that instances of the class carry a [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute, and that the storage for that dictionary is managed by the VM.

When this flag is set, `Py_TPFLAGS_HAVE_GC` should be set as well.

The type's traverse function is required to invoke [`PyObject_VisitManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_VisitManagedDict), and its clear function is required to invoke [`PyObject_ClearManagedDict()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_ClearManagedDict).

Added in version 3.12.

**Inheritance:**

This flag is inherited unless the `tp_dictoffset` field is set in a superclass.

 Py_TPFLAGS_MANAGED_WEAKREF

This bit signals that instances of the class are meant to be weakly referenceable.

Added in version 3.12.

**Inheritance:**

This flag is inherited unless the `tp_weaklistoffset` field is set in a superclass.

 Py_TPFLAGS_ITEMS_AT_END

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Only usable with variable-size types, i.e. ones with non-zero `tp_itemsize`.

Signals that the variable-sized portion of an instance of this type sits at the end of the instance's memory region, at an offset of `Py_TYPE(obj)->tp_basicsize` (which may differ in each subclass).

When you set this flag, make sure that every superclass either follows this same memory layout or else is not variable-sized. Python performs no check of this.

Added in version 3.12.

**Inheritance:**

This flag is inherited.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-flags-to-py-tpflags-default.md) · [Following source contract](py-tpflags-long-subclass-to-py-tpflags-type-subclass.md)
