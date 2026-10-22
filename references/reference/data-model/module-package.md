# module.__package__

module.__package__

The [package](https://docs.python.org/3.14/glossary.html#term-package) within which a module resides.

When a module sits at top level (meaning it belongs to no particular package), this attribute ought to hold `''` (the empty string). In every other case it ought to hold the name of the package that contains the module (which may equal `module.__name__` whenever the module is itself a package). Refer to [**PEP 366**](https://peps.python.org/pep-0366/) for additional information.

Rather than `__name__`, this attribute serves to work out explicit relative imports for main modules. For modules built on the fly via the [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) constructor it defaults to `None`; reach for [`importlib.util.module_from_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.module_from_spec) instead so the attribute ends up holding a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

You are **strongly** advised to reach for [`module.__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent) rather than `module.__package__`. These days `__package__` only kicks in as a fallback when `__spec__.parent` has no value, and that fallback route is deprecated.

Changed in version 3.4: For modules built on the fly via the [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) constructor, this attribute now defaults to `None`. The attribute used to be optional.

Changed in version 3.6: The value held by `__package__` ought to match [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent). These days `__package__` only kicks in as a fallback while resolving imports when `__spec__.parent` carries no definition.

Changed in version 3.10: An [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning) gets raised whenever import resolution drops back to `__package__` rather than [`__spec__.parent`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.parent).

Changed in version 3.12: Raise [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) rather than [`ImportWarning`](https://docs.python.org/3.14/library/exceptions.html#ImportWarning) when dropping back to `__package__` during import resolution.

Deprecated since version 3.13, will be removed in version 3.15: the import system and standard library will stop setting or consulting `__package__`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](import-related-attributes-on-module-objects.md) · [Previous source section](module-spec.md) · [Following source section](module-loader.md)
