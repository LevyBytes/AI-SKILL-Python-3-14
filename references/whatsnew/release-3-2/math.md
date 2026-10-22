# What's New In Python 3.2 / math — math

### math

Drawing on the C99 standard, the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module picked up six additional functions.

A quick and dependable check for special values comes from [`isfinite()`](https://docs.python.org/3.14/library/math.html#math.isfinite). Ordinary numbers yield `True`, while *Nan* or *Infinity* yield `False`:

```python
>>> from math import isfinite
>>> [isfinite(x) for x in (123, 4.56, float('Nan'), float('Inf'))]
[True, True, False, False]

```

For small *x*, [`expm1()`](https://docs.python.org/3.14/library/math.html#math.expm1) evaluates `e**x-1` while sidestepping the precision loss that typically comes from subtracting two nearly identical quantities:

```python
>>> from math import expm1
>>> expm1(0.013671875)   # more accurate way to compute e**x-1 for a small x
0.013765762467652909

```

A probability integral, otherwise called the [Gaussian error function](https://en.wikipedia.org/wiki/Error_function), is evaluated by [`erf()`](https://docs.python.org/3.14/library/math.html#math.erf). Its complement [`erfc()`](https://docs.python.org/3.14/library/math.html#math.erfc) equals `1 - erf(x)`:

```pycon
>>> from math import erf, erfc, sqrt
>>> erf(1.0/sqrt(2.0))   # portion of normal distribution within 1 standard deviation
0.682689492137086
>>> erfc(1.0/sqrt(2.0))  # portion of normal distribution outside 1 standard deviation
0.31731050786291404
>>> erf(1.0/sqrt(2.0)) + erfc(1.0/sqrt(2.0))
1.0

```

Acting as a smooth generalization of the factorial, [`gamma()`](https://docs.python.org/3.14/library/math.html#math.gamma) is described at [https://en.wikipedia.org/wiki/Gamma_function](https://en.wikipedia.org/wiki/Gamma_function). Its tie to factorials means it blows up quickly even at modest *x*, which is why a companion [`lgamma()`](https://docs.python.org/3.14/library/math.html#math.lgamma) exists to return the natural logarithm of the gamma function:

```python
>>> from math import gamma, lgamma
>>> gamma(7.0)           # six factorial
720.0
>>> lgamma(801.0)        # log(800 factorial)
4551.950730698041

```

(Contributed by Mark Dickinson.)

[Subject index](INDEX.md) · [Previous source section](datetime-and-time.md) · [Next source section](abc.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
