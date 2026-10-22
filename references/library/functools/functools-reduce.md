# functools: `functools.reduce()`

functools.reduce(*function*, *iterable*, */*[, *initial*])

Run *function*, which takes two arguments, cumulatively over the entries of *iterable* moving left to right, collapsing the iterable down to one value. As an example, `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` works out `((((1+2)+3)+4)+5)`. The left argument, *x*, holds the running total, while the right argument, *y*, is the next value drawn from the *iterable*. When the optional *initial* is supplied, it sits ahead of the iterable's items during the computation and acts as a fallback should the iterable turn out empty. When *initial* is absent and *iterable* holds just a single item, that first item is what gets returned.

Roughly equivalent to:

```python
initial_missing = object()

def reduce(function, iterable, /, initial=initial_missing):
    it = iter(iterable)
    if initial is initial_missing:
        value = next(it)
    else:
        value = initial
    for element in it:
        value = function(value, element)
    return value

```

Refer to [`itertools.accumulate()`](https://docs.python.org/3.14/library/itertools.html#itertools.accumulate) for an iterator that emits every intermediate value.

Changed in version 3.14: passing *initial* by keyword is now accepted.

[Subject index](INDEX.md) · [Previous](functools-partialmethod-class.md) · [Continue](callable-utilities-signatures-and-contract.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md)
