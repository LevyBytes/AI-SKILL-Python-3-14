# modules C API: Module creation/execution slots and interpreter/GIL declarations

### Module slots

 type PyModuleDef_Slot

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members) since version 3.5.*

 int slot

A slot ID, picked from the values laid out below.

 void *value

Value of the slot, whose meaning depends on the slot ID.

Added in version 3.5.

The available slot types are:

 Py_mod_create

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Names a function invoked so as to build the module object itself. This slot's *value* pointer has to reference a function whose signature reads:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *create_module([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *spec, PyModuleDef *def)

Into the function come a [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) instance, as laid out by [**PEP 451**](https://peps.python.org/pep-0451/), plus the module definition. The function ought to hand back a fresh module object, or else set an error and hand back `NULL`.

Keep this function as small as you can. Above all, it shouldn't run arbitrary Python code, since attempting to re-import the same module could spin into an endless loop.

A single module definition cannot name more than one `Py_mod_create` slot.

Without `Py_mod_create` specified, the import machinery falls back on building an ordinary module object via `PyModule_New()`. The name comes from *spec* rather than the definition, which lets extension modules adapt on the fly to where they sit in the module hierarchy and get imported under various names by way of symlinks, the whole time drawing on a single shared module definition.

The object handed back need not be a `PyModule_Type` instance. Any type works, so long as it permits setting and getting import-related attributes. That said, returning `PyModule_Type` instances is the only option when the `PyModuleDef` carries a non-`NULL` `m_traverse`, `m_clear`, `m_free`; a non-zero `m_size`; or slots beyond `Py_mod_create`.

Added in version 3.5.

 Py_mod_exec

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Names a function invoked so as to *execute* the module. This amounts to running a Python module's code: as a rule, the function loads classes and constants into the module. Here is the function's signature:

 int exec_module([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

When more than one `Py_mod_exec` slot appears, they run in whatever order they sit within the *m_slots* array.

Added in version 3.5.

 Py_mod_multiple_interpreters

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Names one of the following values:

 Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

The module does not support being imported in subinterpreters.

 Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED

The module can be imported in subinterpreters, though only where they share the GIL of the main interpreter. (See [Isolating Extension Modules](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto).)

 Py_MOD_PER_INTERPRETER_GIL_SUPPORTED

The module can be imported in subinterpreters, even those carrying a GIL of their own. (See [Isolating Extension Modules](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto).)

This slot decides whether importing the module inside a subinterpreter ends in failure.

A single module definition cannot name more than one `Py_mod_multiple_interpreters` slot.

Without `Py_mod_multiple_interpreters` specified, the import machinery falls back on `Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED`.

Added in version 3.12.

 Py_mod_gil

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Names one of the following values:

[Subject index](INDEX.md) · [Previous source contract](pymoduledef-to-pymoduledef-type.md) · [Following source contract](py-mod-gil-used-to-py-mod-gil-not-used.md)
