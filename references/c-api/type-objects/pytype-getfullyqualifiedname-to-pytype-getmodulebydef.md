# type objects C API: `PyType_GetFullyQualifiedName()`, `PyType_GetModuleName()`, `PyType_GetSlot()`, `PyType_GetModule()`, `PyType_GetModuleState()`, `PyType_GetModuleByDef()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetFullyQualifiedName(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Returns the type's fully qualified name, the same as `f"{type.__module__}.{type.__qualname__}"`, or just [`type.__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#type.__qualname__) when [`type.__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) is not a string or holds the value `"builtins"`.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetModuleName(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Returns the type's module name, the same as reading the [`type.__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute.

Added in version 3.13.

 void *PyType_GetSlot(PyTypeObject *type, int slot)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.4.*

Returns the function pointer kept in the named slot. A `NULL` result means either the slot itself is `NULL` or the call received invalid parameters. Typically the caller casts the returned pointer to the right function type.

Refer to `PyType_Slot.slot` for the values the *slot* argument may take.

Added in version 3.4.

Changed in version 3.10: `PyType_GetSlot()` will now take any type at all. Earlier on, only [heap types](https://docs.python.org/3.14/c-api/typeobj.html#heap-types) were permitted.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetModule(PyTypeObject *type)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Returns the module object tied to the given type, provided the type was built through `PyType_FromModuleAndSpec()`.

What comes back is a [borrowed](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) reference from *type* that stays valid for as long as you keep a reference to *type*. Never drop it via [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) or anything comparable.

When no module is tied to the given type, the call sets [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and returns `NULL`.

The usual purpose of this function is to obtain the module where a method lives. Be aware that within such a method, `PyType_GetModule(Py_TYPE(self))` might not yield what you expect. `Py_TYPE(self)` could be a *subclass* of the class you mean, and subclasses need not live in the same module as their superclass. Consult [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod) to retrieve the class that defines the method. For situations where `PyCMethod` is unavailable, see `PyType_GetModuleByDef()`.

Added in version 3.9.

 void *PyType_GetModuleState(PyTypeObject *type)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Returns the state of the module object tied to the given type. It is a convenient wrapper around invoking [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState) on whatever `PyType_GetModule()` returns.

When no module is tied to the given type, the call sets [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and returns `NULL`.

When the *type* does have an attached module whose state is `NULL`, the call returns `NULL` without raising an exception.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_GetModuleByDef(PyTypeObject *type, struct [PyModuleDef](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) *def)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Locate the first superclass whose module originated from the supplied [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) *def*, and hand back that module.

When no such module turns up, the call raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and returns `NULL`.

The function is designed to work alongside [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState) to fetch module state from slot methods (for example [`tp_init`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_init) or [`nb_add`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods.nb_add)) and from other spots where a method's defining class can't be supplied through the [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod) calling convention.

What comes back is a [borrowed](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) reference from *type* that stays valid for as long as you keep a reference to *type*. Never drop it via [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) or anything comparable.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-to-pytype-watch.md) · [Previous source contract](pytype-unwatch-to-pytype-getqualname.md) · [Following source contract](pytype-getbasebytoken-to-pytype-supports-weakrefs.md)
