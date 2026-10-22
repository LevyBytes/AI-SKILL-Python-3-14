# object.__bool__(*self*)

object.__bool__(*self*)

Invoked to carry out truth value testing and the built-in operation `bool()`; it should return `False` or `True`. Whenever this method goes undefined, `__len__()` is invoked if it is defined, and the object counts as true whenever its result is nonzero. Should a class define neither `__len__()` nor `__bool__()` (as holds for the [`object`](https://docs.python.org/3.14/library/functions.html#object) class itself), every one of its instances counts as true.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Previous source section](object-hash.md) · [Following source section](customizing-attribute-access.md)
