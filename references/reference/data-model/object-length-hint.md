# object.__length_hint__(*self*)

object.__length_hint__(*self*)

Invoked to back [`operator.length_hint()`](https://docs.python.org/3.14/library/operator.html#operator.length_hint). It should hand back an estimated length for the object (which can come out higher or lower than the true length). That length has to be an integer `>=` 0. Returning [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) is also permitted, and it is handled exactly as though the `__length_hint__` method were absent entirely. The method serves only as an optimization and is never needed for correctness.

Added in version 3.4.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Following source section](object-len.md) · [Previous source section](object-len.md) · [Following source section](object-getitem.md)
