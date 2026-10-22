# Python 3.13.0 alpha 1 / c api / module

[gh-107226](https://github.com/python/cpython/issues/107226): Access to [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef) is now restricted to limited API version 3.10 and newer.

[bpo-42327](https://bugs.python.org/issue?@action=redirect&bpo=42327): Introduce the [`PyModule_Add()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_Add) function. It resembles [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef) and [`PyModule_AddObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObject), but it consistently steals a reference to the supplied value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
