# module.__loader__

module.__loader__

The [loader](https://docs.python.org/3.14/glossary.html#term-loader) object that the import machinery employed to load the module.

The chief value of this attribute is for introspection, though it can serve loader-specific purposes too, such as retrieving data tied to a loader.

For modules built on the fly via the [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) constructor, `__loader__` defaults to `None`; reach for [`importlib.util.module_from_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.module_from_spec) instead so the attribute ends up holding a [loader](https://docs.python.org/3.14/glossary.html#term-loader) object.

You are **strongly** advised to reach for [`module.__spec__.loader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.loader) rather than `module.__loader__`.

Changed in version 3.4: For modules built on the fly via the [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) constructor, this attribute now defaults to `None`. The attribute used to be optional.

Deprecated since version 3.12, will be removed in version 3.16: It is deprecated to set `__loader__` on a module while leaving `__spec__.loader` unset. As of Python 3.16, `__loader__` will no longer be set or consulted by the import system or the standard library.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](import-related-attributes-on-module-objects.md) · [Previous source section](module-package.md) · [Following source section](module-path.md)
