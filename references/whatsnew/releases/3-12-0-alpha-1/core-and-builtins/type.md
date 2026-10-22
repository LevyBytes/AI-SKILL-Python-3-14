# Python 3.12.0 alpha 1 / core and builtins / type

[gh-93012](https://github.com/python/cpython/issues/93012): Introduced the new [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass) function, a generalization of the current [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) that takes one extra metaclass argument. Language binding tools find this handy, since it lets them hook type-related operations — subclassing or static attribute access, for instance — by naming a metaclass that supplies custom slots.

Crucially, [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass) ships in the Limited API, opening a route for moving additional binding tools onto the Stable ABI.

[gh-96046](https://github.com/python/cpython/issues/96046): [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) now sets up `ht_cached_keys` and runs extra checks confirming that type objects are configured correctly. That heads off crashes in 3rd party packages that bypass the regular API when creating new types.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
