# object.__set__(*self*, *instance*, *value*)

object.__set__(*self*, *instance*, *value*)

Invoked so that, on an owner-class instance *instance*, the attribute takes on a fresh value, *value*.

Be aware that introducing `__set__()` or `__delete__()` shifts the descriptor’s kind to a “data descriptor”. Consult Invoking Descriptors for fuller detail.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Owning language section](implementing-descriptors.md) · [Previous source section](object-get.md) · [Following source section](object-delete.md)
