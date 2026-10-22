# Python 3.10.0 alpha 3 / c api / module

[bpo-1635741](https://bugs.python.org/issue?@action=redirect&bpo=1635741): Brought in the [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef) function, akin to [`PyModule_AddObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObject) yet not stealing a reference to the value when it succeeds. Victor Stinner authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
