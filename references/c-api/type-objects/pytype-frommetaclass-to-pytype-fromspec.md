# type objects C API: `PyType_FromMetaclass()`, `PyType_FromModuleAndSpec()`, `PyType_FromSpecWithBases()`, `PyType_FromSpec()`

### Creating Heap-Allocated Types

The functions and structs below exist to build [heap types](https://docs.python.org/3.14/c-api/typeobj.html#heap-types).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_FromMetaclass(PyTypeObject *metaclass, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, PyType_Spec *spec, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bases)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Build and return a [heap type](https://docs.python.org/3.14/c-api/typeobj.html#heap-types) out of the *spec* (refer to [`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE)).

The resulting type object is constructed using the metaclass *metaclass*. Should *metaclass* be `NULL`, the metaclass comes from *bases* (or from the *Py_tp_base[s]* slots when *bases* is `NULL`, as described below).

Metaclasses that override [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) are not supported, except if `tp_new` is `NULL`.

Use the *bases* argument to name base classes; it accepts either a single class or a tuple of classes. When *bases* is `NULL`, the [`Py_tp_bases`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_bases) slot stands in for it. When that too is `NULL`, the [`Py_tp_base`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_tp_base) slot stands in. And when that too is `NULL`, the new type inherits from [`object`](https://docs.python.org/3.14/library/functions.html#object).

Use the *module* argument to note the module where the new class lives. It has to be a module object or `NULL`. When it is not `NULL`, the module gets tied to the new type and can be fetched afterward via `PyType_GetModule()`. Subclasses do not inherit the attached module; you have to set it on each class one at a time.

This function runs `PyType_Ready()` on the new type.

Bear in mind that this function does *not* completely reproduce the effect of invoking [`type()`](https://docs.python.org/3.14/library/functions.html#type) or writing a [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) statement. When user-supplied base types or metaclasses are involved, favor [calling](https://docs.python.org/3.14/c-api/call.html#capi-call) `type` (or the metaclass) rather than the `PyType_From*` functions. In particular:

- On the new class, [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) goes uninvoked (and its value has to be `type.__new__`).

- [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) is not called on the new class.

- [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) is not called on any bases.

- [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) is not called on new descriptors.

Added in version 3.12.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_FromModuleAndSpec([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, PyType_Spec *spec, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bases)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

The same as `PyType_FromMetaclass(NULL, module, spec, bases)`.

Added in version 3.9.

Changed in version 3.10: A lone class is now permitted for the *bases* argument, and `NULL` is permitted for the `tp_doc` slot.

Changed in version 3.12: The function now locates and applies a metaclass that matches the base classes you supply. Up to that point, what came back was always a [`type`](https://docs.python.org/3.14/library/functions.html#type) instance.

The metaclass's [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) gets *ignored*. which can leave initialization unfinished. Building classes where the metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: It is no longer permitted to build classes where the metaclass overrides [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_FromSpecWithBases(PyType_Spec *spec, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *bases)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.3.*

The same as `PyType_FromMetaclass(NULL, NULL, spec, bases)`.

Added in version 3.3.

Changed in version 3.12: The function now locates and applies a metaclass that matches the base classes you supply. Up to that point, what came back was always a [`type`](https://docs.python.org/3.14/library/functions.html#type) instance.

The metaclass's [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) gets *ignored*. which can leave initialization unfinished. Building classes where the metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: It is no longer permitted to build classes where the metaclass overrides [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyType_FromSpec(PyType_Spec *spec)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The same as `PyType_FromMetaclass(NULL, NULL, spec, NULL)`.

Changed in version 3.12: The function now locates and applies a metaclass that matches whichever base classes appear in the *Py_tp_base[s]* slots. Up to that point, what came back was always a [`type`](https://docs.python.org/3.14/library/functions.html#type) instance.

The metaclass's [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) gets *ignored*. which can leave initialization unfinished. Building classes where the metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: It is no longer permitted to build classes where the metaclass overrides [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new).

[Subject index](INDEX.md) · [Previous source contract](pytype-getbasebytoken-to-pytype-supports-weakrefs.md) · [Following source contract](pytype-freeze.md)
