# Python 3.14.0 beta 1 / c api / type

[gh-133166](https://github.com/python/cpython/issues/133166): A regression is fixed where [`PyType_GetModuleByDef()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleByDef), when handed a static type, returned NULL without setting [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
