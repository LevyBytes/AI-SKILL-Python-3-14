# modules C API: `PyModuleDef`, `PyModuleDef_Type`

type PyModuleDef

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members).*

The module definition struct carries everything required to build a module object. You must allocate this structure statically (or otherwise ensure it stays valid for as long as any modules built from it survive). As a rule, each extension module has just one variable of this type.

 PyModuleDef_Base m_base

This member must always be initialized to `PyModuleDef_HEAD_INIT`.

 const char *m_name

Name for the new module.

 const char *m_doc

The module's docstring; the usual choice is a docstring variable produced with [`PyDoc_STRVAR`](https://docs.python.org/3.14/c-api/intro.html#c.PyDoc_STRVAR).

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) m_size

Rather than living in static globals, module state can sit in a per-module memory area that `PyModule_GetState()` retrieves. Doing so keeps modules safe to use across multiple sub-interpreters.

The size of *m_size* governs how much of this area gets allocated at module creation, and it is freed once the module object is deallocated, after `m_free` (if there is one) has run.

A non-negative value here signals that the module supports re-initialization and tells the system the extra memory its state demands.

Assigning `-1` to `m_size` signals that the module won't work with sub-interpreters, owing to its global state. A negative `m_size` is permitted solely with [legacy single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization), or when modules are built dynamically.

Consult [**PEP 3121**](https://peps.python.org/pep-3121/) for further detail.

 [PyMethodDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) *m_methods

Points at a table of the module's top-level functions, each one specified through [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) values. Where no functions exist, this may be `NULL`.

 PyModuleDef_Slot *m_slots

A list of slot definitions supporting multi-phase initialization, ending with a `{0, NULL}` entry. With legacy single-phase initialization in play, *m_slots* has to be `NULL`.

Changed in version 3.5: Ahead of release 3.5, this member stayed fixed at `NULL`, with the following definition:

>

 [inquiry](https://docs.python.org/3.14/c-api/gcsupport.html#c.inquiry) m_reload

 [traverseproc](https://docs.python.org/3.14/c-api/gcsupport.html#c.traverseproc) m_traverse

A traversal routine invoked while the module object is traversed during GC, or `NULL` where none is required.

It is skipped if module state was asked for yet isn't allocated so far. That happens right after the module is created and ahead of the module being executed (the `Py_mod_exec` function). To be exact, the call is skipped when `m_size` exceeds 0 while the module state (what `PyModule_GetState()` reports) is `NULL`.

Changed in version 3.9: Invocation no longer happens until after the module's state has been allocated.

 [inquiry](https://docs.python.org/3.14/c-api/gcsupport.html#c.inquiry) m_clear

A clearing routine invoked while the module object is cleared during GC, or `NULL` where none is required.

It is skipped if module state was asked for yet isn't allocated so far. That happens right after the module is created and ahead of the module being executed (the `Py_mod_exec` function). To be exact, the call is skipped when `m_size` exceeds 0 while the module state (what `PyModule_GetState()` reports) is `NULL`.

As with [`PyTypeObject.tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear), this routine isn't *always* invoked ahead of a module's deallocation. To illustrate, when reference counting alone suffices to show an object is no longer in use, the cyclic garbage collector stays out of it and `m_free` runs directly.

Changed in version 3.9: The call now waits until the module's state has been allocated.

 [freefunc](https://docs.python.org/3.14/c-api/typeobj.html#c.freefunc) m_free

A routine invoked while the module object is being deallocated, or `NULL` where none is required.

It is skipped if module state was asked for yet isn't allocated so far. That happens right after the module is created and ahead of the module being executed (the `Py_mod_exec` function). To be exact, the call is skipped when `m_size` exceeds 0 while the module state (what `PyModule_GetState()` reports) is `NULL`.

Changed in version 3.9: Allocation of the module's state now precedes any such call.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyModuleDef_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

The type of `PyModuleDef` objects.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](module-definitions.md) · [Following source contract](pymoduledef-slot-to-py-mod-gil.md)
