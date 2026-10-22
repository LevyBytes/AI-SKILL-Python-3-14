# types: `types.ModuleType`, `importlib.util.module_from_spec()`

*class *types.ModuleType(*name*, *doc=None*)

The type of [modules](https://docs.python.org/3.14/glossary.html#term-module). The constructor accepts the name for the module to be created and, optionally, its [docstring](https://docs.python.org/3.14/glossary.html#term-docstring).

See also

[Documentation on module objects](https://docs.python.org/3.14/reference/datamodel.html#module-objects)

Covers the details of the special attributes you may find on instances of `ModuleType`.

[`importlib.util.module_from_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.module_from_spec)

A module built through the `ModuleType` constructor comes into being with many of its special attributes unset or holding default values. `module_from_spec()` offers a sturdier route for creating `ModuleType` instances that makes certain the various attributes end up set correctly.

[Subject index](INDEX.md) · [Previous](types-methoddescriptortype-to-types-classmethoddescriptortype.md) · [Continue](types-ellipsistype-class.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
