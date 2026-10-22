# modules C API: `PyModule_AddStringConstant()`, `PyModule_AddIntMacro()`, `PyModule_AddStringMacro()`, `PyModule_AddType()`, `PyModule_AddFunctions()`, `PyModule_SetDocString()`, `PyUnstable_Module_SetGIL()`

int PyModule_AddStringConstant([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *name, const char *value)

* Lives in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Register a string constant on *module* under *name*. You may call this convenience function from inside the module’s initialization function. The string *value* has to end in `NULL`. It returns `-1` along with a set exception on error, or `0` when it succeeds.

Acting as a convenience wrapper, it invokes [`PyUnicode_InternFromString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_InternFromString) and `PyModule_AddObjectRef()`; consult their documentation for the specifics.

 PyModule_AddIntMacro(module, macro)

Register an int constant on *module*. Both the name and the value come straight from *macro*. To illustrate, `PyModule_AddIntMacro(module, AF_INET)` places onto *module* the int constant *AF_INET* carrying the value of *AF_INET*. It returns `-1` along with a set exception on error, or `0` when it succeeds.

 PyModule_AddStringMacro(module, macro)

Register a string constant on *module*.

 int PyModule_AddType([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type)

* Has belonged to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) ever since version 3.10.*

Register a type object on *module*. That type object gets finalized through an internal call to [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready). Its name is drawn from whatever follows the final dot in [`tp_name`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_name). It returns `-1` along with a set exception on error, or `0` when it succeeds.

Added in version 3.9.

 int PyModule_AddFunctions([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, [PyMethodDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) *functions)

* Has belonged to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) ever since version 3.7.*

Register on *module* the functions held in the `NULL` terminated *functions* array. Turn to the [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) documentation for what each entry means (because there is no shared module namespace, C-implemented module level “functions” are usually handed the module as their first parameter, which makes them resemble instance methods found on Python classes).

When a module is built out of `PyModuleDef` (for example via [Multi-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#multi-phase-initialization), `PyModule_Create`, or `PyModule_FromDefAndSpec`), this function runs on its own. Certain module authors may rather spread their function definitions across several [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) arrays; should they do so, they need to invoke this function themselves.

Static allocation of the *functions* array is mandatory (or you must otherwise ensure it lasts longer than the module object).

Added in version 3.5.

 int PyModule_SetDocString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *docstring)

* Joined the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) at version 3.7.*

Assign *docstring* as the docstring belonging to *module*. When a module is built out of `PyModuleDef` (for example via [Multi-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#multi-phase-initialization), `PyModule_Create`, or `PyModule_FromDefAndSpec`), this function runs on its own.

A `0` comes back on success. On error it returns `-1` with an exception set.

Added in version 3.5.

 int PyUnstable_Module_SetGIL([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, void *gil)

 *This counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Minor releases may alter it with no warning given.*

Signal whether or not *module* can run with the global interpreter lock (GIL) absent, by passing one of the `Py_mod_gil` values. Under [Legacy single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization), the call has to happen inside *module*’s initialization function. Omit this call during module initialization and the import machinery presumes the module cannot operate without the GIL. Only Python builds set up with [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil) expose this function. It returns `-1` along with a set exception on error, or `0` when it succeeds.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymodule-addobjectref-to-pymodule-add.md) · [Previous source contract](pymodule-addintconstant.md) · [Following source contract](pystate-findmodule-to-pystate-removemodule.md)
