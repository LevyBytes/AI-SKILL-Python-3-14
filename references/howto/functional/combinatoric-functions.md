# Combinatoric functions

### Combinatoric functions

The [`itertools.combinations(iterable, r)`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations) yields an iterator producing every possible *r*-tuple combination drawn from the elements held in *iterable*.

```python
itertools.combinations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 3), (2, 4), (2, 5),
  (3, 4), (3, 5),
  (4, 5)

itertools.combinations([1, 2, 3, 4, 5], 3) =>
  (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5),
  (2, 3, 4), (2, 3, 5), (2, 4, 5),
  (3, 4, 5)

```

Within each tuple the elements keep the order in which *iterable* delivered them. To illustrate, the number 1 always precedes 2, 3, 4, or 5 throughout the examples above. A close cousin, [`itertools.permutations(iterable, r=None)`](https://docs.python.org/3.14/library/itertools.html#itertools.permutations), drops this ordering restriction and yields every possible arrangement of length *r*:

```python
itertools.permutations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 1), (2, 3), (2, 4), (2, 5),
  (3, 1), (3, 2), (3, 4), (3, 5),
  (4, 1), (4, 2), (4, 3), (4, 5),
  (5, 1), (5, 2), (5, 3), (5, 4)

itertools.permutations([1, 2, 3, 4, 5]) =>
  (1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
  ...
  (5, 4, 3, 2, 1)

```

Omit a value for *r* and the iterable's own length applies, so that the whole set of elements gets permuted.

Be aware that these functions generate all the possible combinations based on position and place no requirement that the contents of *iterable* be unique:

```python
itertools.permutations('aba', 3) =>
  ('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'),
  ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')

```

The same tuple `('a', 'a', 'b')` shows up twice here, yet the two 'a' strings originated at different positions.

The [`itertools.combinations_with_replacement(iterable, r)`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations_with_replacement) function loosens a different restriction: an element may recur inside one tuple. Think of it as choosing an element for the tuple's first slot and then putting it back before the second element gets chosen.

```python
itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2) =>
  (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 2), (2, 3), (2, 4), (2, 5),
  (3, 3), (3, 4), (3, 5),
  (4, 4), (4, 5),
  (5, 5)

```

[Subject index](INDEX.md) · [Previous source context](selecting-elements.md) · [Following source context](grouping-elements.md)
