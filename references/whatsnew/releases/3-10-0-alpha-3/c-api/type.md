# Python 3.10.0 alpha 3 / c api / type

[bpo-41073](https://bugs.python.org/issue?@action=redirect&bpo=41073): Static types are now valid input for [`PyType_GetSlot()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetSlot).

[bpo-42423](https://bugs.python.org/issue?@action=redirect&bpo=42423): A lone class is now acceptable as the *bases* argument for the [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) and [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) functions.

[bpo-41832](https://bugs.python.org/issue?@action=redirect&bpo=41832): A NULL `tp_doc` slot is now tolerated by the [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
