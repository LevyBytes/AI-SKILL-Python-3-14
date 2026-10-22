# object.__setitem__(*self*, *key*, *value*)

object.__setitem__(*self*, *key*, *value*)

Invoked to back assignment to `self[key]`. The same note applies as with `__getitem__()`. Implement this only for mappings when the objects permit altering the values bound to keys, or when new keys may be added, or for sequences when elements may be substituted. The same exceptions should be raised for invalid *key* values as for the `__getitem__()` method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](object-getitem.md) · [Following source section](object-delitem.md)
