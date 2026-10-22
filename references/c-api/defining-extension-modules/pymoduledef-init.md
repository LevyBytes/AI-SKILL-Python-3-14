# Multi-phase initialization

### Multi-phase initialization

In the typical case, the initialization function (`PyInit_modulename`) hands back a [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) instance whose [`m_slots`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_slots) is non-`NULL`. Prior to being returned, that `PyModuleDef` instance has to be set up by means of the function below:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModuleDef_Init([PyModuleDef](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) *def)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Makes certain that a module definition is a Python object initialized the right way, one that accurately reports both its type and a reference count.

Hands back *def* cast as `PyObject*`, or `NULL` should an error have occurred.

Invoking this function is mandatory for Multi-phase initialization, and it ought not to be applied anywhere else.

Keep in mind that Python treats `PyModuleDef` structures as statically allocated. The function might give back a new reference or a borrowed one; either way, that reference must never be released.

Added in version 3.5.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](defining-extension-modules.md) · [Previous source contract](pyinit-modulename-to-pymodinit-func.md) · [Following source contract](legacy-single-phase-initialization.md)
