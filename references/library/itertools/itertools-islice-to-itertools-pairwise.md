# itertools: `itertools.islice()`, `itertools.pairwise()`

itertools.islice(*iterable*, *stop*)

 itertools.islice(*iterable*, *start*, *stop*[, *step*])

Make an iterator that hands back chosen elements out of the iterable. It behaves like slicing a sequence, except it rejects negative values for *start*, *stop*, or *step*.

Where *start* is zero or `None`, iteration kicks off at zero. Otherwise, elements coming from the iterable get skipped over until *start* is hit.

Where *stop* is `None`, iteration runs on until the input is spent, if that ever happens. Otherwise, it halts once the given position is reached.

Where *step* is `None`, it defaults to one. Elements arrive one after another unless *step* is given a value above one, in which case some items get skipped.

Roughly equivalent to:

```python
def islice(iterable, *args):
    # islice('ABCDEFG', 2) → A B
    # islice('ABCDEFG', 2, 4) → C D
    # islice('ABCDEFG', 2, None) → C D E F G
    # islice('ABCDEFG', 0, None, 2) → A C E G

    s = slice(*args)
    start = 0 if s.start is None else s.start
    stop = s.stop
    step = 1 if s.step is None else s.step
    if start < 0 or (stop is not None and stop < 0) or step <= 0:
        raise ValueError

    indices = count() if stop is None else range(max(start, stop))
    next_i = start
    for i, element in zip(indices, iterable):
        if i == next_i:
            yield element
            next_i += step

```

Should the input be an iterator, then draining the *islice* completely moves the input iterator forward by `max(start, stop)` steps no matter what the *step* value happens to be.

 itertools.pairwise(*iterable*)

Return successive overlapping pairs taken from the input *iterable*.

How many 2-tuples land in the output iterator will be one less than the number of inputs. The output stays empty whenever the input iterable holds fewer than two values.

Roughly equivalent to:

```python
def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG

    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](itertools-filterfalse-to-itertools-groupby.md) · [Continue](itertools-permutations-to-itertools-product.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
