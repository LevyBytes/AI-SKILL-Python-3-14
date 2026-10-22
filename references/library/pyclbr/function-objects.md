# pyclbr: Function browser source-file and definition metadata

file

Name of the file the function is defined in.

 module

The name of the module defining the function described.

 name

The name of the function.

 lineno

The line number inside the file where the definition begins.

 parent

For top-level functions, `None`. For nested functions, the parent.

Added in version 3.7.

 children

A [`dictionary`](https://docs.python.org/3.14/library/stdtypes.html#dict) mapping names to descriptors for nested functions and classes.

Added in version 3.7.

 is_async

`True` for functions defined with the [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) prefix, `False` otherwise.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](pyclbr-function-class.md) · [Continue](pyclbr-class-class.md) · [Owning module, declaration or section: pyclbr](pyclbr-readmodule-to-pyclbr-readmodule-ex.md) · [Owning module, declaration or section: pyclbr.Function](pyclbr-function-class.md) · [Owning module, declaration or section: Function Objects](pyclbr-function-class.md)
