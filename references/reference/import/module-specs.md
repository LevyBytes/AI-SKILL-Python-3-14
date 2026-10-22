# 5.4.3. Module specs

### 5.4.3. Module specs

While importing each module — particularly in the stage preceding loading — the import machinery relies on assorted details about it. The bulk of that data is shared across every module. A module spec exists to bundle up this import-related data on a module-by-module basis.

Employing a spec throughout an import lets state move between the components of the import system, for instance from the finder that builds the module spec to the loader that runs it. Crucially, it lets the import machinery carry out the repetitive work of loading, which without a module spec would have fallen to the loader.

A module's spec shows up as [`module.__spec__`](https://docs.python.org/3.14/reference/datamodel.html#module.__spec__). Configuring `__spec__` properly holds true as well for [modules initialized during interpreter startup](https://docs.python.org/3.14/reference/toplevel_components.html#programs). The lone exception is `__main__`, whose `__spec__` ends up set to None under certain conditions.

Refer to [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) for specifics about what a module spec holds.

Added in version 3.4.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](submodules.md) · [Following source section](path-attributes-on-modules.md)
