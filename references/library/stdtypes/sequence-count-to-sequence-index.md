# Common Sequence Operations

sequence.count(*value*, */*)

Return how many times *value* occurs in *sequence* altogether.

 sequence.index(*value*[, *start*[, *stop*]])

Return the index where *value* first appears within *sequence*.

Raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *value* is absent from *sequence*.

The *start* and *stop* arguments make it possible to search sections of the sequence efficiently, starting from *start* and finishing at *stop*. This roughly matches `start + sequence[start:stop].index(value)`, except that no data gets copied.

Caution

The *start* and *stop* arguments are not accepted by every sequence type.

[Subject index](INDEX.md) · [Previous](sequence-negative-slice-boundaries.md) · [Continue](immutable-sequence-types.md) · [Owning module, declaration or section: Common Sequence Operations](sequence-operations-overview.md)
