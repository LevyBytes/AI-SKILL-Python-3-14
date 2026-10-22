# What’s New In Python 3.8 / math — math

> (Suggested by Raymond Hettinger, implemented by Donghee Na, and reviewed by Vinay Sajip in [bpo-33897](https://bugs.python.org/issue?@action=redirect&bpo=33897).)

### math

A fresh [`math.dist()`](https://docs.python.org/3.14/library/math.html#math.dist) function has been added for figuring the Euclidean distance separating a pair of points.
> (Contributed by Raymond Hettinger in [bpo-33089](https://bugs.python.org/issue?@action=redirect&bpo=33089).)

The [`math.hypot()`](https://docs.python.org/3.14/library/math.html#math.hypot) function has grown to cope with several dimensions. Up to now it only managed the 2-D case.
> (Contributed by Raymond Hettinger in [bpo-33089](https://bugs.python.org/issue?@action=redirect&bpo=33089).)

A fresh function, [`math.prod()`](https://docs.python.org/3.14/library/math.html#math.prod), arrives as a counterpart to [`sum()`](https://docs.python.org/3.14/library/functions.html#sum); it yields a "start" value (defaulting to 1) multiplied across an iterable of numbers:

```python
>>> prior = 0.8
>>> likelihoods = [0.625, 0.84, 0.30]
>>> math.prod(likelihoods, start=prior)
0.126

```

> (Contributed by Pablo Galindo in [bpo-35606](https://bugs.python.org/issue?@action=redirect&bpo=35606).)

A pair of fresh combinatoric functions, [`math.perm()`](https://docs.python.org/3.14/library/math.html#math.perm) and [`math.comb()`](https://docs.python.org/3.14/library/math.html#math.comb), have been added:

```python
>>> math.perm(10, 3)    # Permutations of 10 things taken 3 at a time
720
>>> math.comb(10, 3)    # Combinations of 10 things taken 3 at a time
120

```

> (Contributed by Yash Aggarwal, Keller Fuchs, Serhiy Storchaka, and Raymond Hettinger in [bpo-37128](https://bugs.python.org/issue?@action=redirect&bpo=37128), [bpo-37178](https://bugs.python.org/issue?@action=redirect&bpo=37178), and [bpo-35431](https://bugs.python.org/issue?@action=redirect&bpo=35431).)

A fresh [`math.isqrt()`](https://docs.python.org/3.14/library/math.html#math.isqrt) function has been added for computing exact integer square roots while never converting to floating point. This new function copes with arbitrarily large integers. It outruns `floor(sqrt(n))` though it trails [`math.sqrt()`](https://docs.python.org/3.14/library/math.html#math.sqrt):

```python
>>> r = 650320427
>>> s = r ** 2
>>> isqrt(s - 1)         # correct
650320426
>>> floor(sqrt(s - 1))   # incorrect
650320427

```

> (Contributed by Mark Dickinson in [bpo-36887](https://bugs.python.org/issue?@action=redirect&bpo=36887).)

Arguments that are not int-like are no longer tolerated by the [`math.factorial()`](https://docs.python.org/3.14/library/math.html#math.factorial) function.

[Subject index](INDEX.md) · [Previous source section](logging.md) · [Next source section](mmap.md) · [Release/subject declaration](assignment-expressions.md)
