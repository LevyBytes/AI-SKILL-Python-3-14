# itertools: `itertools.zip_longest()`

Because of the flattening behavior, tee iterators can be peeked at efficiently:

```python
def lookahead(tee_iterator):
     "Return the next value without moving the input forward"
     [forked_iterator] = tee(tee_iterator, 1)
     return next(forked_iterator)

```

```pycon
>>> iterator = iter('abcdef')
>>> [iterator] = tee(iterator, 1)   # Make the input peekable
>>> next(iterator)                  # Move the iterator forward
'a'
>>> lookahead(iterator)             # Check next value
'b'
>>> next(iterator)                  # Continue moving forward
'b'

```

`tee` iterators are not threadsafe. Using the iterators from a single `tee()` call at the same time can raise a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), even when the original *iterable* is itself threadsafe.

Depending on the amount of temporary data that has to be held, this itertool can need a fair bit of auxiliary storage. As a rule, when one iterator consumes most or all of the data ahead of another starting, calling [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) is faster than `tee()`.

 itertools.zip_longest(**iterables*, *fillvalue=None*)

Build an iterator that gathers elements drawn from each of the *iterables*.

Where the iterables differ in length, the gaps get padded with *fillvalue*. When left unspecified, *fillvalue* defaults to `None`.

Iteration keeps going until the longest of the iterables runs out.

Roughly equivalent to:

```python
def zip_longest(*iterables, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-

    iterators = list(map(iter, iterables))
    num_active = len(iterators)
    if not num_active:
        return

    while True:
        values = []
        for i, iterator in enumerate(iterators):
            try:
                value = next(iterator)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

```

When any of the iterables could be infinite, wrap the `zip_longest()` function in something that caps how many calls happen (for instance `islice()` or `takewhile()`).

[Subject index](INDEX.md) · [Continue](itertools-recipes-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md) · [Owning module, declaration or section: itertools.tee](itertools-tee.md) · [Preceding source contract and version conditions](itertools-tee.md)
