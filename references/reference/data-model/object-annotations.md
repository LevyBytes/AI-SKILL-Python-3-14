# object.__annotations__

object.__annotations__

This attribute holds the annotations for an object. It is [lazily evaluated](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation), so reading the attribute may run arbitrary code and raise exceptions. When evaluation succeeds, the attribute is set to a dictionary that maps variable names to annotations.

Changed in version 3.14: Annotations are now lazily evaluated.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](annotations.md) · [Previous source section](annotations.md) · [Following source section](object-annotate.md)
