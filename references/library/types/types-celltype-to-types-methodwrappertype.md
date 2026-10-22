# types: `types.CellType`, `types.MethodType`, `types.BuiltinFunctionType`, `types.BuiltinMethodType`, `types.WrapperDescriptorType`, `types.MethodWrapperType`

types.CellType

The type for cell objects: objects of this kind act as containers holding a function’s [closure variables](https://docs.python.org/3.14/glossary.html#term-closure-variable).

Added in version 3.8.

 types.MethodType

The type of the methods belonging to user-defined class instances.

 types.BuiltinFunctionType

 types.BuiltinMethodType

The type of built-in functions such as [`len()`](https://docs.python.org/3.14/library/functions.html#len) or [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit), along with methods of built-in classes. (In this context, “built-in” stands for “written in C”.)

 types.WrapperDescriptorType

The type of methods belonging to certain built-in data types and base classes, [`object.__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) or [`object.__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__) among them.

Added in version 3.7.

 types.MethodWrapperType

The type of the *bound* methods of certain built-in data types and base classes. As an example, it is the type of `object().__str__`.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](types-codetype-class.md) · [Continue](types-notimplementedtype-class.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
