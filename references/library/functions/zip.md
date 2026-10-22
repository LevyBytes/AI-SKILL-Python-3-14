# zip

zip(**iterables*, *strict=False*)

Step through several iterables together, yielding tuples that hold one item drawn from each.

Example:

```python
>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
...     print(item)
...
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

```

Put more precisely: `zip()` hands back an iterator of tuples, in which the *i*-th tuple gathers the *i*-th element out of each argument iterable.

Yet another way to picture `zip()` is as flipping rows into columns and columns into rows. The effect resembles [transposing a matrix](https://en.wikipedia.org/wiki/Transpose).

`zip()` works lazily: nothing gets processed until the iterable is actually iterated, say through a `for` loop or by passing it into a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list).

Bear in mind that the iterables you feed to `zip()` may differ in length — at times intentionally, at times owing to a bug in whatever code built those iterables. Python gives you three distinct ways to handle that situation:

- By default, `zip()` halts once the shortest iterable runs dry. The leftover items in the longer iterables are dropped, trimming the result down to the length of the shortest iterable:

```python
>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]

```

-

A frequent use of `zip()` arises when the iterables are presumed to share a common length. For those situations, supplying the `strict=True` option is advised. The result matches that of an ordinary `zip()` call:

```python
>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
[('a', 1), ('b', 2), ('c', 3)]

```

Departing from the standard behavior, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised should any one iterable run out ahead of the rest:

```python
>>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
...     print(item)
...
(0, 'fee')
(1, 'fi')
(2, 'fo')
Traceback (most recent call last):
  ...
ValueError: zip() argument 2 is longer than argument 1

```

If you omit the `strict=True` argument, a defect that produces iterables of mismatched lengths goes unnoticed, and it may surface later as an elusive bug elsewhere in your program.

- To bring every iterable up to a uniform length, the shorter ones may be filled out using a fixed value. The [`itertools.zip_longest()`](https://docs.python.org/3.14/library/itertools.html#itertools.zip_longest) function handles this.

Edge cases: Given just one iterable argument, `zip()` yields an iterator of 1-tuples; given none at all, the iterator it returns is empty.

Tips and tricks:

- Iterables are guaranteed to be evaluated in left-to-right order. That guarantee enables an idiom that gathers a data series into n-length groups by means of `zip(*[iter(s)]*n, strict=True)`. Here the *same* iterator is repeated `n` times, which makes every output tuple hold the outcome of `n` successive calls to that iterator. The net result is to split the input into n-length chunks.

- Pairing `zip()` together with the `*` operator lets you unzip a list:

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True

```

Changed in version 3.10: The `strict` argument was introduced.

[Builtin task index](INDEX.md).
