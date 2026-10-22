# any, all and zip consumption rules

The [`any(iter)`](https://docs.python.org/3.14/library/functions.html#any) and [`all(iter)`](https://docs.python.org/3.14/library/functions.html#all) built-ins inspect the truth values of whatever an iterable holds. `any()` yields `True` when at least one item in the iterable is truthy, while `all()` yields `True` only when every item is truthy:

```python
>>> any([0, 1, 0])
True
>>> any([0, 0, 0])
False
>>> any([1, 1, 1])
True
>>> all([0, 1, 0])
False
>>> all([0, 0, 0])
False
>>> all([1, 1, 1])
True

```

[`zip(iterA, iterB, ...)`](https://docs.python.org/3.14/library/functions.html#zip) draws a single item from every iterable and packages them together inside a tuple:

```python
zip(['a', 'b', 'c'], (1, 2, 3)) =>
  ('a', 1), ('b', 2), ('c', 3)

```

It does not build a list in memory or drain all of its source iterators up front; rather, each tuple is assembled and handed back only when it is asked for. (The formal name for this kind of behaviour is [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation).)

The expectation is that you feed this iterator iterables that share the same length. Should the iterables differ in length, the produced stream runs only as long as the shortest of them.

```python
zip(['a', 'b'], (1, 2, 3)) =>
  ('a', 1), ('b', 2)

```

It's best to steer clear of this, however, since an item might be pulled from the longer iterators and then thrown away. As a consequence you cannot keep using those iterators afterward, because you might skip over a discarded item.

[Subject index](INDEX.md) · [map and filter transformations](map-and-filter-transformations.md) · [enumerate positions and sorted output](enumerate-positions-and-sorted-output.md) · [Previous source context](enumerate-positions-and-sorted-output.md) · [Following source context](the-itertools-module.md)
