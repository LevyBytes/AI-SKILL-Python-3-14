# object.__delitem__(*self*, *key*)

object.__delitem__(*self*, *key*)

Invoked to back deletion of `self[key]`. The same note applies as with `__getitem__()`. Implement this only for mappings when the objects permit removing keys, or for sequences when elements may be deleted from the sequence. The same exceptions should be raised for invalid *key* values as for the `__getitem__()` method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](object-setitem.md) · [Following source section](object-missing.md)
