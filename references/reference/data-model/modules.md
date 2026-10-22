# 3.2.9. Modules

### 3.2.9. Modules

A basic structural building block of Python code is the module, which the [import system](https://docs.python.org/3.14/reference/import.html#importsystem) produces in response either to the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement or to calls of functions like [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) and the built-in [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__). Each module object carries a namespace backed by a [`dictionary`](https://docs.python.org/3.14/library/stdtypes.html#dict) object (this is the very dictionary that the `__globals__` attribute of functions defined within the module points at). Attribute references map onto lookups within that dictionary; for example, `m.x` amounts to `m.__dict__["x"]`. The code object that initialized the module is not retained by the module object (because there is no use for it once initialization has finished).

Assigning to an attribute writes into the module’s namespace dictionary; for example, `m.x = 1` amounts to `m.__dict__["x"] = 1`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](class-instances.md) · [Following source section](import-related-attributes-on-module-objects.md)
