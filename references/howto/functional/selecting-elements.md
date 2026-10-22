# Selecting elements

### Selecting elements

A further set of functions picks a subset of an iterator's elements according to a predicate.

[`itertools.filterfalse(predicate, iter)`](https://docs.python.org/3.14/library/itertools.html#itertools.filterfalse) inverts [`filter()`](https://docs.python.org/3.14/library/functions.html#filter), yielding every element for which the predicate comes back false:

```python
itertools.filterfalse(is_even, itertools.count()) =>
  1, 3, 5, 7, 9, 11, 13, 15, ...

```

[`itertools.takewhile(predicate, iter)`](https://docs.python.org/3.14/library/itertools.html#itertools.takewhile) keeps yielding elements as long as the predicate stays true. The moment the predicate turns false, the iterator marks the end of its output.

```python
def less_than_10(x):
    return x < 10

itertools.takewhile(less_than_10, itertools.count()) =>
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9

itertools.takewhile(is_even, itertools.count()) =>
  0

```

[`itertools.dropwhile(predicate, iter)`](https://docs.python.org/3.14/library/itertools.html#itertools.dropwhile) throws away elements for as long as the predicate stays true, and afterward yields the remainder of the iterable's output.

```python
itertools.dropwhile(less_than_10, itertools.count()) =>
  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...

itertools.dropwhile(is_even, itertools.count()) =>
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...

```

[`itertools.compress(data, selectors)`](https://docs.python.org/3.14/library/itertools.html#itertools.compress) accepts two iterators and yields only the items of *data* whose matching item in *selectors* is true, halting as soon as either of them runs out:

```python
itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True]) =>
   1, 2, 5

```

[Subject index](INDEX.md) · [Previous source context](calling-functions-on-elements.md) · [Following source context](combinatoric-functions.md)
