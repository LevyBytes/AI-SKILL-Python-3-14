# What’s New in Python 2.6 / New and Improved Modules — itertools, logging, math, mmap, operator

```python
>>> list(itertools.permutations([1,2,3,4], 2))
[(1, 2), (1, 3), (1, 4),
 (2, 1), (2, 3), (2, 4),
 (3, 1), (3, 2), (3, 4),
 (4, 1), (4, 2), (4, 3)]

```

`itertools.chain(*iterables)` is a function already present in [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) that received a new constructor in Python 2.6. `itertools.chain.from_iterable(iterable)` accepts one iterable that is expected to yield further iterables. `chain()` then yields all the elements from the first iterable, followed by all from the second, and so forth.

```python
>>> list(itertools.chain.from_iterable([[1,2,3], [4,5,6]]))
[1, 2, 3, 4, 5, 6]

```

(All contributed by Raymond Hettinger.)

- The `FileHandler` class of the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module, plus its subclasses `WatchedFileHandler`, `RotatingFileHandler`, and `TimedRotatingFileHandler`, now take an optional *delay* parameter in their constructors. When *delay* is true, the log file is not opened until the first `emit()` call happens. (Contributed by Vinay Sajip.)

`TimedRotatingFileHandler` additionally takes a *utc* constructor parameter. When that argument is true, UTC time drives the determination of when midnight falls and the generation of filenames; if not, local time is used instead.

- A handful of new functions joined the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module:

  - [`isinf()`](https://docs.python.org/3.14/library/math.html#math.isinf) and [`isnan()`](https://docs.python.org/3.14/library/math.html#math.isnan) tell you, respectively, whether some given float counts as an infinity (positive or negative) or instead as a NaN (Not a Number).

  - [`copysign()`](https://docs.python.org/3.14/library/math.html#math.copysign) transfers the sign bit of an IEEE 754 number, yielding the absolute value of *x* paired with the sign bit of *y*. As an example, `math.copysign(1, -0.0)` returns -1.0. (Contributed by Christian Heimes.)

  - [`factorial()`](https://docs.python.org/3.14/library/math.html#math.factorial) works out the factorial of a number. (Contributed by Raymond Hettinger; [bpo-2138](https://bugs.python.org/issue?@action=redirect&bpo=2138).)

  - [`fsum()`](https://docs.python.org/3.14/library/math.html#math.fsum) totals up the stream of numbers coming from an iterable, taking care to dodge loss of precision by keeping partial sums. (Contributed by Jean Brouwers, Raymond Hettinger, and Mark Dickinson; [bpo-2819](https://bugs.python.org/issue?@action=redirect&bpo=2819).)

  - [`acosh()`](https://docs.python.org/3.14/library/math.html#math.acosh), [`asinh()`](https://docs.python.org/3.14/library/math.html#math.asinh) and [`atanh()`](https://docs.python.org/3.14/library/math.html#math.atanh) work out the inverse hyperbolic functions.

  - [`log1p()`](https://docs.python.org/3.14/library/math.html#math.log1p) hands back the natural logarithm of *1+x* (base *e*).

  - `trunc()` rounds a number in the direction of zero, returning the nearest `Integral` lying between the function’s argument and zero. It was added as part of backporting PEP 3141’s type hierarchy for numbers.

- The [`math`](https://docs.python.org/3.14/library/math.html#module-math) module was reworked to behave more uniformly from one platform to another, particularly around how it deals with floating-point exceptions and IEEE 754 special values.

Wherever it can, the module sticks to what the C99 standard advises about 754’s special values. For instance, `sqrt(-1.)` should now raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) on nearly every platform, whereas `sqrt(float('NaN'))` should hand back a NaN on every IEEE 754 platform. Where Annex ‘F’ of the C99 standard calls for signaling ‘divide-by-zero’ or ‘invalid’, Python raises `ValueError`. Where Annex ‘F’ of the C99 standard calls for signaling ‘overflow’, Python raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). (See [bpo-711019](https://bugs.python.org/issue?@action=redirect&bpo=711019) and [bpo-1640](https://bugs.python.org/issue?@action=redirect&bpo=1640).)

(Contributed by Christian Heimes and Mark Dickinson.)

- [`mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) objects now carry a `rfind()` method that hunts for a substring starting from the end of the string and scanning backwards. The `find()` method likewise picked up an *end* parameter supplying an index at which to halt the search. (Contributed by John Lenton.)

- The [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module gained a `methodcaller()` function that accepts a name plus an optional collection of arguments, returning a callable that invokes the named function on whatever arguments are handed to it. As an example:

```python
>>> # Equivalent to lambda s: s.replace('old', 'new')
>>> replacer = operator.methodcaller('replace', 'old', 'new')
>>> replacer('old wine in old bottles')
'new wine in new bottles'

```

(Contributed by Georg Brandl, after a suggestion by Gregory Petrosyan.)

[Subject index](INDEX.md) · [Previous source section](heapq-through-itertools-module-changes.md) · [Next source section](attribute-lookup-and-process-module-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md)
