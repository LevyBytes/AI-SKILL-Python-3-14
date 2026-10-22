# annotationlib: `annotationlib.type_repr()`

annotationlib.type_repr(*value*)

Turn an arbitrary Python value into a form fit for the `STRING` format to use. For the majority of objects this invokes [`repr()`](https://docs.python.org/3.14/library/functions.html#repr), though certain objects — type objects among them — receive special treatment.

It is intended as a helper for user-written annotate functions that handle the `STRING` format yet have no access to the code that builds the annotations. You can equally apply it to produce a friendly string representation for other objects holding values that crop up often in annotations.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](annotationlib-get-annotations.md) · [Continue](using-annotations-in-a-metaclass.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Owning module, declaration or section: Functions](annotation-string-conversion-and-evaluation.md)
