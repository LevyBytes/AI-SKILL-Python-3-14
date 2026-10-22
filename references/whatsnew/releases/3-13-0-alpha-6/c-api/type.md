# Python 3.13.0 alpha 6 / c api / type

[gh-116936](https://github.com/python/cpython/issues/116936): Bring [`PyType_GetModuleByDef()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleByDef) into the limited C API. Victor Stinner wrote the patch.

[gh-111696](https://github.com/python/cpython/issues/111696): Introduce the [`PyType_GetModuleName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleName) function for fetching a type's module name. It amounts to reading the `type.__module__` attribute. Eric Snow and Victor Stinner wrote the patch.

[gh-111696](https://github.com/python/cpython/issues/111696): Introduce the [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetFullyQualifiedName) function for fetching a type's fully qualified name. It is the same as `f"{type.__module__}.{type.__qualname__}"`, or just `type.__qualname__` when `type.__module__` is not a string or equals `"builtins"`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
