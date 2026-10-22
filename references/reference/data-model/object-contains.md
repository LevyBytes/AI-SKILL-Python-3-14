# object.__contains__(*self*, *item*)

object.__contains__(*self*, *item*)

Invoked to back membership test operators. It should return true when *item* is found in *self*, false otherwise. For mapping objects, the membership check ought to inspect the mapping's keys instead of its values or its key-item pairs.

For objects lacking a `__contains__()` definition, the membership test first attempts iteration through `__iter__()`, then the older sequence iteration protocol through `__getitem__()`; see [this section in the language reference](https://docs.python.org/3.14/reference/expressions.html#membership-test-details).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](object-reversed.md) · [Following source section](emulating-numeric-types.md)
