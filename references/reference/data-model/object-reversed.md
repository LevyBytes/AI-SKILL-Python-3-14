# object.__reversed__(*self*)

object.__reversed__(*self*)

Invoked (when present) by the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) built-in to back reverse iteration. It should hand back a fresh iterator object that traverses every object in the container in reverse order.

When the `__reversed__()` method is absent, the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) built-in resorts to the sequence protocol (`__len__()` and `__getitem__()`). Objects backing the sequence protocol ought to supply `__reversed__()` only when they can deliver an implementation more efficient than the one `reversed()` supplies.

The membership test operators ([`in`](https://docs.python.org/3.14/reference/expressions.html#in) and [`not in`](https://docs.python.org/3.14/reference/expressions.html#not-in)) are usually backed by iterating across a container. Container objects, however, can offer the following special method with a more efficient implementation, which additionally removes the requirement that the object be iterable.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](object-iter.md) · [Following source section](object-contains.md)
