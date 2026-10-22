# itertools: `itertools.compress()`, `itertools.count()`, `itertools.cycle()`, `itertools.dropwhile()`

itertools.compress(*data*, *selectors*)

Make an iterator that hands back items from *data* wherever the matching entry in *selectors* evaluates true. It halts as soon as either the *data* or the *selectors* iterable runs out. Roughly equivalent to:

```python
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
    return (datum for datum, selector in zip(data, selectors) if selector)

```

Added in version 3.1.

 itertools.count(*start=0*, *step=1*)

Make an iterator that hands back evenly spaced values starting from *start*. Pair it with [`map()`](https://docs.python.org/3.14/library/functions.html#map) to produce successive data points, or with [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) to attach sequence numbers. Roughly equivalent to:

```python
def count(start=0, step=1):
    # count(10) → 10 11 12 13 14 ...
    # count(2.5, 0.5) → 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

```

While counting using floating-point numbers, you can occasionally get sharper accuracy by swapping in multiplicative code along the lines of: `(start + step * i for i in count())`.

Changed in version 3.1: The *step* argument was introduced, and non-integer arguments became permitted.

 itertools.cycle(*iterable*)

Make an iterator that hands back elements from the *iterable* while keeping a copy of each one. Once the iterable is spent, it begins handing back elements out of that saved copy. This goes on without end. Roughly equivalent to:

```python
def cycle(iterable):
    # cycle('ABCD') → A B C D A B C D A B C D ...

    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element

```

Depending on how long the iterable is, this itertool can demand a considerable amount of extra storage.

 itertools.dropwhile(*predicate*, *iterable*)

Make an iterator that discards elements from the *iterable* for as long as the *predicate* stays true, and from then on yields each remaining element. Roughly equivalent to:

```python
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,3,8]) → 6 3 8

    iterator = iter(iterable)
    for x in iterator:
        if not predicate(x):
            yield x
            break

    for x in iterator:
        yield x

```

Be aware that nothing at all gets emitted until the predicate turns false for the first time, which can give this itertool a slow start-up.

[Subject index](INDEX.md) · [Previous](iterator-combinations-and-replacement.md) · [Continue](itertools-filterfalse-to-itertools-groupby.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
