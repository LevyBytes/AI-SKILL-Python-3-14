# Python 3.9.0 alpha 5 / c api / module

[bpo-40024](https://bugs.python.org/issue?@action=redirect&bpo=40024): Provide the [`PyModule_AddType()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddType) helper function, which adds a type to a module. Donghee Na supplied the patch.

[bpo-39824](https://bugs.python.org/issue?@action=redirect&bpo=39824): Extension modules: the [`m_traverse`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_traverse), [`m_clear`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_clear) and [`m_free`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_free) functions belonging to [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) are no longer invoked once the module state has been requested yet not allocated. That situation arises right after a module is created and prior to its execution (the [`Py_mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function). To be precise, these functions go uncalled when [`m_size`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_size) exceeds 0 while the module state (per [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState)) is `NULL`.

Modules that lack module state (`m_size <= 0`) remain unaffected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
