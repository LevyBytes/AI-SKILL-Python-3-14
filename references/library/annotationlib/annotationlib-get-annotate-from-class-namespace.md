# annotationlib: `annotationlib.get_annotate_from_class_namespace()`

annotationlib.get_annotate_from_class_namespace(*namespace*)

Pull the [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function) out of a class namespace dictionary *namespace*. Hand back `None` if that namespace holds no annotate function. This proves most handy before the class has finished being created (for example, inside a metaclass); once the class is in existence, you can obtain its annotate function via `cls.__annotate__`. An example of applying this function within a metaclass appears below.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](annotation-string-conversion-and-evaluation.md) · [Continue](annotationlib-get-annotations.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Owning module, declaration or section: Functions](annotation-string-conversion-and-evaluation.md)
