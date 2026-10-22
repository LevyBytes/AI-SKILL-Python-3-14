# Creating extension modules dynamically

### Creating extension modules dynamically

The functions below can build a module beyond an extension's [initialization function](https://docs.python.org/3.14/c-api/extension-modules.html#extension-export-hook). They likewise come into play during [single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_Create(PyModuleDef *def)

*Return value: New reference.*

Build a fresh module object from the definition supplied in *def*. This macro invokes `PyModule_Create2()` with *module_api_version* set to `PYTHON_API_VERSION`, or set to `PYTHON_ABI_VERSION` whenever the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) is in use.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_Create2(PyModuleDef *def, int module_api_version)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a fresh module object from the definition supplied in *def*, taking the API version to be *module_api_version*. Should that version differ from the running interpreter's version, a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) is emitted.

On error, `NULL` is returned together with an exception set.

Slots aren't supported by this function. The *def* `m_slots` member has to be `NULL`.

Note

Nearly every use of this function ought to go through `PyModule_Create()` instead; reach for this one only when you're certain it's needed.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_FromDefAndSpec(PyModuleDef *def, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *spec)

*Return value: New reference.*

This macro invokes `PyModule_FromDefAndSpec2()` with *module_api_version* set to `PYTHON_API_VERSION`, or set to `PYTHON_ABI_VERSION` whenever the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) is in use.

Added in version 3.5.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_FromDefAndSpec2(PyModuleDef *def, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *spec, int module_api_version)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Build a fresh module object from the definition supplied in *def* alongside the ModuleSpec *spec*, taking the API version to be *module_api_version*. Should that version differ from the running interpreter's version, a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) is emitted.

On error, `NULL` is returned together with an exception set.

Be aware that execution slots (`Py_mod_exec`) go unprocessed here. To fully initialize a module, both `PyModule_FromDefAndSpec` and `PyModule_ExecDef` have to be called.

Note

Nearly every use of this function ought to go through `PyModule_FromDefAndSpec()` instead; reach for this one only when you're certain it's needed.

Added in version 3.5.

 int PyModule_ExecDef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, PyModuleDef *def)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Handle whatever execution slots (`Py_mod_exec`) appear in *def*.

Added in version 3.5.

 PYTHON_API_VERSION

The C API version. Defined for backwards compatibility.

As things stand, this constant goes unchanged across new Python releases, and it serves no purpose for versioning. That could shift down the road.

 PYTHON_ABI_VERSION

Defined as `3` for backwards compatibility.

As things stand, this constant goes unchanged across new Python releases, and it serves no purpose for versioning. That could shift down the road.

[Subject index](INDEX.md) · [Previous source contract](py-mod-gil-used-to-py-mod-gil-not-used.md) · [Following source contract](pymodule-addobjectref-to-pymodule-add.md)
