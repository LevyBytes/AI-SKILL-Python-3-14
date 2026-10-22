# itertools: `itertools.repeat()`, `itertools.starmap()`, `itertools.takewhile()`

itertools.repeat(*object*[, *times*])

Make an iterator that keeps returning the same *object* again and again. It carries on endlessly unless you give the *times* argument.

Roughly equivalent to:

```python
def repeat(object, times=None):
    # repeat(10, 3) → 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

```

One frequent application of *repeat* is feeding a stream of unchanging values into *map* or *zip*:

```pycon
>>> list(map(pow, range(10), repeat(2)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

 itertools.starmap(*function*, *iterable*)

Make an iterator that evaluates the *function* with arguments pulled from the *iterable*. Use it in place of [`map()`](https://docs.python.org/3.14/library/functions.html#map) when the argument parameters are already "pre-zipped" together into tuples.

How [`map()`](https://docs.python.org/3.14/library/functions.html#map) differs from `starmap()` mirrors the gap between `function(a,b)` and `function(*c)`. Roughly equivalent to:

```python
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000
    for args in iterable:
        yield function(*args)

```

 itertools.takewhile(*predicate*, *iterable*)

Make an iterator that keeps yielding elements from the *iterable* for as long as the *predicate* holds true. Roughly equivalent to:

```python
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,3,8]) → 1 4
    for x in iterable:
        if not predicate(x):
            break
        yield x

```

Take note that the first element to fail the predicate test gets pulled off the input iterator, with no way left to retrieve it. That may cause trouble if an application means to keep drawing from the input iterator once *takewhile* has been exhausted. As a workaround for this, think about using [more-itertools before_and_after()](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.before_and_after) instead.

[Subject index](INDEX.md) · [Previous](itertools-permutations-to-itertools-product.md) · [Continue](itertools-tee.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
