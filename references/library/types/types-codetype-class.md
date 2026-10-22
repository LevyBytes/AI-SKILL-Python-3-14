# types: `types.CodeType`

*class *types.CodeType(***kwargs*)

The type of [code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects) like those that [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) returns.

Emits an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `code.__new__` carrying the arguments `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags`.

Keep in mind that the audited arguments need not line up with the names or positions the initializer expects. The audit event fires solely on direct instantiation of code objects; it is not emitted during ordinary compilation.

[Subject index](INDEX.md) · [Previous](types-nonetype-class-to-types-asyncgeneratortype.md) · [Continue](types-celltype-to-types-methodwrappertype.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
