# map and filter transformations

### Built-in functions

Now let's examine more closely the built-in functions that frequently pair with iterators.

A pair of Python built-ins, [`map()`](https://docs.python.org/3.14/library/functions.html#map) and [`filter()`](https://docs.python.org/3.14/library/functions.html#filter), reproduce what generator expressions already do:

[`map(f, iterA, iterB, ...)`](https://docs.python.org/3.14/library/functions.html#map) yields an iterator across the sequence

`f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ...`.

```python
>>> def upper(s):
...     return s.upper()

```

```python
>>> list(map(upper, ['sentence', 'fragment']))
['SENTENCE', 'FRAGMENT']
>>> [upper(s) for s in ['sentence', 'fragment']]
['SENTENCE', 'FRAGMENT']

```

Naturally, a list comprehension lets you reach the very same outcome.

[`filter(predicate, iter)`](https://docs.python.org/3.14/library/functions.html#filter) yields an iterator across every element of the sequence satisfying a given test, and list comprehensions likewise mirror it. A **predicate** denotes a function reporting the truth value of a condition; when paired with `filter()`, that predicate has to accept exactly one value.

```python
>>> def is_even(x):
...     return (x % 2) == 0

```

```python
>>> list(filter(is_even, range(10)))
[0, 2, 4, 6, 8]

```

The equivalent list comprehension form is:

```python
>>> list(x for x in range(10) if is_even(x))
[0, 2, 4, 6, 8]

```

[Subject index](INDEX.md) · [enumerate positions and sorted output](enumerate-positions-and-sorted-output.md) · [any, all and zip consumption rules](any-all-and-zip-consumption-rules.md) · [Previous source context](passing-values-into-a-generator-continuation.md) · [Following source context](enumerate-positions-and-sorted-output.md)
