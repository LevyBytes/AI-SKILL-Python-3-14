# pyclbr: Class browser source-file and definition metadata

file

Name of the file the class is defined in.

 module

The name of the module defining the class described.

 name

The name of the class.

 lineno

The line number inside the file where the definition begins.

 parent

For top-level classes, `None`. For nested classes, the parent.

Added in version 3.7.

 children

A dictionary mapping names to descriptors for nested functions and classes.

Added in version 3.7.

 super

A list of `Class` objects describing the immediate base classes of the class being described. Classes named as superclasses yet not discoverable by `readmodule_ex()` show up as a string carrying the class name rather than as `Class` objects.

 methods

A [`dictionary`](https://docs.python.org/3.14/library/stdtypes.html#dict) mapping method names to line numbers. This can be drawn from the newer `children` dictionary, yet survives for back-compatibility.

[Subject index](INDEX.md) · [Previous](pyclbr-class-class.md) · [Continue](../pydoc/pydoc-documentation-generator-and-online-help-system.md) · [Owning module, declaration or section: pyclbr](pyclbr-readmodule-to-pyclbr-readmodule-ex.md) · [Owning module, declaration or section: pyclbr.Class](pyclbr-class-class.md) · [Owning module, declaration or section: Class Objects](pyclbr-class-class.md)
