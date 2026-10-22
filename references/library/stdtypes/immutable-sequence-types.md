# Immutable Sequence Types

### Immutable Sequence Types

What immutable sequence types generally provide that mutable ones do not is support for the [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) built-in.

Thanks to this, immutable sequences — `tuple` instances, say — can act as `dict` keys and be held in `set` and `frozenset` instances.

Trying to hash an immutable sequence holding unhashable values produces a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[Subject index](INDEX.md) · [Previous](sequence-count-to-sequence-index.md) · [Continue](sequence-append-to-sequence-reverse.md)
