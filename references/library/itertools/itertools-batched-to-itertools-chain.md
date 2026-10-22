# itertools: `itertools.batched()`, `itertools.chain()`, `chain.from_iterable()`

itertools.batched(*iterable*, *n*, ***, *strict=False*)

Gather data drawn from the *iterable* into tuples whose length is *n*. That closing batch might run shorter than *n*.

When *strict* is true, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised should the closing batch come up shorter than *n*.

It iterates across the supplied iterable, gathering items into tuples that grow up to *n* in size. Consumption of the input happens lazily, drawing only what a batch needs. Each batch is handed back the moment it reaches *n*, or once the input iterable runs dry:

```pycon
>>> flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
>>> unflattened = list(batched(flattened_data, 2))
>>> unflattened
[('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]

```

Roughly equivalent to:

```python
def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch

```

Added in version 3.12.

Changed in version 3.13: Added the *strict* option.

 itertools.chain(**iterables*)

Make an iterator that draws elements from the first iterable until nothing remains, then moves on to the following iterable, continuing this way until every iterable has run out. This fuses several data sources together as one iterator. Roughly equivalent to:

```python
def chain(*iterables):
    # chain('ABC', 'DEF') → A B C D E F
    for iterable in iterables:
        yield from iterable

```

 *classmethod *chain.from_iterable(*iterable*)

Alternate constructor for `chain()`. Pulls the chained inputs out of one iterable argument, evaluating it lazily. Roughly equivalent to:

```python
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) → A B C D E F
    for iterable in iterables:
        yield from iterable

```

[Subject index](INDEX.md) · [Previous](itertools-accumulate.md) · [Continue](iterator-combinations-and-replacement.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
