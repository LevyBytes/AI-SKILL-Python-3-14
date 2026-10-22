# 3.2.9.1. Import-related attributes on module objects

#### 3.2.9.1. Import-related attributes on module objects

Each module object carries the attributes below that pertain to the [import system](https://docs.python.org/3.14/reference/import.html#importsystem). Whenever a module is built by the machinery tied to the import system, these attributes get populated from the module’s [spec](https://docs.python.org/3.14/glossary.html#term-module-spec) before the [loader](https://docs.python.org/3.14/glossary.html#term-loader) runs and loads the module.

When you want to build a module on the fly rather than going through the import system, the recommended approach is [`importlib.util.module_from_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.module_from_spec), which assigns suitable values to the various import-governed attributes. The [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) constructor can also build modules directly, yet that route invites more mistakes, since with it most attributes have to be set by hand on the module object once it exists.

Caution

Apart from `__name__`, you are **strongly** advised to depend on `__spec__` and the attributes it carries rather than any of the separate attributes enumerated in this subsection. Be aware that changing an attribute on `__spec__` does not propagate the change to the matching attribute on the module itself:

```pycon
>>> import typing
>>> typing.__name__, typing.__spec__.name
('typing', 'typing')
>>> typing.__spec__.name = 'spelling'
>>> typing.__name__, typing.__spec__.name
('typing', 'spelling')
>>> typing.__name__ = 'keyboard_smashing'
>>> typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling')

```

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Previous source section](modules.md) · [Following source section](module-name.md)
