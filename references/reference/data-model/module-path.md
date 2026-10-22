# module.__path__

module.__path__

A [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of strings (possibly empty) listing the places where the package’s submodules are to be located. Modules that are not packages ought not to carry a `__path__` attribute. Consult [__path__ attributes on modules](https://docs.python.org/3.14/reference/import.html#package-path-rules) for further information.

You are **strongly** advised to reach for [`module.__spec__.submodule_search_locations`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.submodule_search_locations) rather than `module.__path__`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](import-related-attributes-on-module-objects.md) · [Previous source section](module-loader.md) · [Following source section](module-file-module-cached.md)
