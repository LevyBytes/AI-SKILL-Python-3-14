# Creating new iterators

### Creating new iterators

[`itertools.count(start, step)`](https://docs.python.org/3.14/library/itertools.html#itertools.count) hands back an endless stream of uniformly spaced values. You may optionally pass the first number, defaulting to 0, along with the gap between values, defaulting to 1:

```python
itertools.count() =>
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
itertools.count(10) =>
  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...
itertools.count(10, 5) =>
  10, 15, 20, 25, 30, 35, 40, 45, 50, 55, ...

```

[`itertools.cycle(iter)`](https://docs.python.org/3.14/library/itertools.html#itertools.cycle) keeps a copy of everything in a supplied iterable and produces a new iterator that walks its items from first through last. That new iterator loops over these items forever.

```python
itertools.cycle([1, 2, 3, 4, 5]) =>
  1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...

```

[`itertools.repeat(elem, [n])`](https://docs.python.org/3.14/library/itertools.html#itertools.repeat) hands back the supplied element *n* times, or, when *n* is omitted, repeats the element forever.

```python
itertools.repeat('abc') =>
  abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...
itertools.repeat('abc', 5) =>
  abc, abc, abc, abc, abc

```

[`itertools.chain(iterA, iterB, ...)`](https://docs.python.org/3.14/library/itertools.html#itertools.chain) accepts any number of iterables and yields every element of the first iterator, followed by every element of the second, continuing on until all the iterables are drained.

```python
itertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>
  a, b, c, 1, 2, 3

```

[`itertools.islice(iter, [start], stop, [step])`](https://docs.python.org/3.14/library/itertools.html#itertools.islice) hands back a stream that forms a slice of the iterator. Given just a *stop* argument, it produces the leading *stop* elements. Provide a starting index and you receive *stop-start* elements, and provide a *step* value and elements get skipped to match. In contrast to slicing Python strings and lists, negative numbers are not allowed for *start*, *stop*, or *step*.

```python
itertools.islice(range(10), 8) =>
  0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
  2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
  2, 4, 6

```

[`itertools.tee(iter, [n])`](https://docs.python.org/3.14/library/itertools.html#itertools.tee) clones an iterator; it yields *n* separate iterators, each of which will deliver the contents of the original iterator. When you omit a value for *n*, it defaults to 2. Cloning iterators means stashing some of the original iterator's contents, so memory use can climb sharply when the iterator is big and one of the new iterators races ahead of the others.

```python
itertools.tee( itertools.count() ) =>
   iterA, iterB

where iterA ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

and   iterB ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

```

[Subject index](INDEX.md) · [Previous source context](the-itertools-module.md) · [Following source context](calling-functions-on-elements.md)
