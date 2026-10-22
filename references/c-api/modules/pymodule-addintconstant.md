# int PyModule_AddIntConstant(PyObject *module, const char *name, long value)

int PyModule_AddIntConstant([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, const char *name, long value)

* Sits within the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Register an integer constant on *module* under *name*. You may call this convenience function from inside the module’s initialization function. It returns `-1` along with a set exception on error, or `0` when it succeeds.

Acting as a convenience wrapper, it invokes [`PyLong_FromLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromLong) and `PyModule_AddObjectRef()`; consult their documentation for the specifics.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymodule-addobjectref-to-pymodule-add.md) · [Following source contract](pymodule-addobject.md) · [Following source contract](pymodule-addstringconstant-to-pyunstable-module-setgil.md)
