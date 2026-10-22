# 3.2.5. Sequences

### 3.2.5. Sequences

These stand for finite, ordered collections indexed by non-negative numbers. The built-in function [`len()`](https://docs.python.org/3.14/library/functions.html#len) gives back how many items a sequence holds. With a sequence of length *n*, the set of indices runs over the numbers 0, 1, …, *n*-1. Item *i* of sequence *a* is picked out by `a[i]`. A number of sequences, the built-in ones included, read negative subscripts by adding the sequence length to them. As an illustration, with sequence a of length `n`, `a[-2]` matches `a[n-2]`, namely the next-to-last item.

Whatever value results must be a nonnegative integer below the count of items the sequence holds. Should it fall outside that, an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) is raised.

Slicing is supported by sequences too: `a[start:stop]` picks out every item whose index *k* satisfies *start* `<=` *k* `<` *stop*. Used within an expression, a slice yields a sequence of the same type. That same earlier point about negative subscripts applies to negative slice positions too. Be aware that a slice position below zero, or beyond the sequence's length, triggers no error at all.

When *start* is absent or [`None`](https://docs.python.org/3.14/library/constants.html#None), slicing acts as though *start* were zero. When *stop* is absent or `None`, slicing acts as though *stop* equaled the length of the sequence.

A number of sequences additionally support “extended slicing” by way of a third “step” parameter: `a[i:j:k]` picks out every item of *a* whose index *x* satisfies `x = i + n*k`, *n* `>=` `0` and *i* `<=` *x* `<` *j*.

Sequences fall into two groups based on whether they are mutable:

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](numbers-complex.md) · [Following source section](immutable-sequences.md)
