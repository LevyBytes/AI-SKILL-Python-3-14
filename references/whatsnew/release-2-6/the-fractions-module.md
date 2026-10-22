# What’s New in Python 2.6 / The `fractions` Module — fractions

### The [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) Module

Rounding out the numeric type hierarchy, the [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) module supplies a rational-number class. A rational number holds its value as a numerator together with a denominator that make up a fraction, so it can represent a value like `2/3` exactly — something floating-point numbers can merely approximate.

Two `Integral` values, which become the numerator and the denominator of the produced fraction, are what the `Fraction` constructor expects.

```python
>>> from fractions import Fraction
>>> a = Fraction(2, 3)
>>> b = Fraction(2, 5)
>>> float(a), float(b)
(0.66666666666666663, 0.40000000000000002)
>>> a+b
Fraction(16, 15)
>>> a/b
Fraction(5, 3)

```

To turn floating-point numbers into rationals, the float type now carries an `as_integer_ratio()` method that hands back the numerator and denominator of a fraction equal to the very same floating-point value:

```python
>>> (2.5) .as_integer_ratio()
(5, 2)
>>> (3.1415) .as_integer_ratio()
(7074029114692207L, 2251799813685248L)
>>> (1./3) .as_integer_ratio()
(6004799503160661L, 18014398509481984L)

```

Bear in mind that a value floating-point can only approximate, such as 1./3, is not reduced to whatever number it is approximating; instead the fraction works to reproduce the floating-point value **exactly**.

The [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) module grew out of an implementation by Sjoerd Mullender that had lived in Python’s `Demo/classes/` directory for years. Jeffrey Yasskin gave that implementation a substantial overhaul.

[Subject index](INDEX.md) · [Previous source section](pep-3141-a-type-hierarchy-for-numbers.md) · [Next source section](core-language-changes.md) · [Release/subject declaration](python-3-0.md)
