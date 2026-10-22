# itertools: `itertools.accumulate()`

### Itertool Functions

Each function listed here builds and hands back an iterator. A few of them yield endless streams, so reach for them only via helpers or loops that cut the stream off at some point.

 itertools.accumulate(*iterable*[, *function*, ***, *initial=None*])

Make an iterator yielding running sums, or running results computed by some other binary function.

By default the *function* performs addition. It is expected to take two arguments — a running total so far and the next value drawn from the *iterable*.

When an *initial* value gets supplied, accumulation begins from that value, and as a result the output carries one extra element compared with the input iterable.

Roughly equivalent to:

```python
def accumulate(iterable, function=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) → 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) → 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) → 1 2 6 24 120

    iterator = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(iterator)
        except StopIteration:
            return

    yield total
    for element in iterator:
        total = function(total, element)
        yield total

```

For a running minimum, point *function* at [`min()`](https://docs.python.org/3.14/library/functions.html#min); for a running maximum, point it at [`max()`](https://docs.python.org/3.14/library/functions.html#max); and for a running product, point it at [`operator.mul()`](https://docs.python.org/3.14/library/operator.html#operator.mul). You can also generate an [amortization table](https://www.ramseysolutions.com/real-estate/amortization-schedule) by accumulating the interest while subtracting each payment:

```pycon
>>> data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> list(accumulate(data, max))              # running maximum
[3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
>>> list(accumulate(data, operator.mul))     # running product
[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]

# Amortize a 5% loan of 1000 with 10 annual payments of 90
>>> update = lambda balance, payment: round(balance * 1.05) - payment
>>> list(accumulate(repeat(90, 10), update, initial=1_000))
[1000, 960, 918, 874, 828, 779, 728, 674, 618, 559, 497]

```

A comparable function that hands back only the last accumulated value is [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce).

Added in version 3.2.

Changed in version 3.3: Added the optional *function* parameter.

Changed in version 3.8: Added the optional *initial* parameter.

[Subject index](INDEX.md) · [Previous](itertools-functions-creating-iterators-for-efficient-looping.md) · [Continue](itertools-batched-to-itertools-chain.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md)
