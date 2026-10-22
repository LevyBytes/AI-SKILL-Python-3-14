# fractions / Rational numbers: `as_integer_ratio()`, `is_integer()`, `from_float()`, `from_decimal()`, `from_number()`, `limit_denominator()`, `__floor__()`, `__ceil__()`

numerator

The Fraction's numerator, reduced to lowest terms.

 denominator

The Fraction's denominator, reduced to lowest terms. It is always positive.

 as_integer_ratio()

Hands back a two-integer tuple whose ratio matches the original Fraction. That ratio sits in lowest terms with a positive denominator.

Added in version 3.8.

 is_integer()

Hands back `True` whenever the Fraction happens to be an integer.

Added in version 3.12.

 *classmethod *from_float(*f*)

A secondary constructor that takes nothing but instances of [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`numbers.Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral). Watch out: `Fraction.from_float(0.3)` does not equal the value `Fraction(3, 10)`.

Note

As of Python 3.2, building a `Fraction` instance straight from a [`float`](https://docs.python.org/3.14/library/functions.html#float) is possible as well.

 *classmethod *from_decimal(*dec*)

A secondary constructor that takes nothing but instances of [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) or [`numbers.Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral).

Note

Beginning with Python 3.2, you may likewise build a `Fraction` instance straight from a [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instance.

 *classmethod *from_number(*number*)

A secondary constructor that takes only instances of [`numbers.Integral`](https://docs.python.org/3.14/library/numbers.html#numbers.Integral), [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational), [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal), along with objects bearing the `as_integer_ratio()` method — though strings are excluded.

Added in version 3.14.

 limit_denominator(*max_denominator=1000000*)

Locates and hands back the `Fraction` nearest to `self` whose denominator stays at or below max_denominator. The method earns its keep when you need rational approximations of some floating-point number:

```python
>>> from fractions import Fraction
>>> Fraction('3.1415926535897932').limit_denominator(1000)
Fraction(355, 113)

```

or for recovering a rational number that’s represented as a float:

```python
>>> from math import pi, cos
>>> Fraction(cos(pi/3))
Fraction(4503599627370497, 9007199254740992)
>>> Fraction(cos(pi/3)).limit_denominator()
Fraction(1, 2)
>>> Fraction(1.1).limit_denominator()
Fraction(11, 10)

```

 __floor__()

Hands back the largest [`int`](https://docs.python.org/3.14/library/functions.html#int) that is `<= self`. You can also get at this method by way of the [`math.floor()`](https://docs.python.org/3.14/library/math.html#math.floor) function:

```python
>>> from math import floor
>>> floor(Fraction(355, 113))
3

```

 __ceil__()

Hands back the smallest [`int`](https://docs.python.org/3.14/library/functions.html#int) that is `>= self`. You can also get at this method by way of the [`math.ceil()`](https://docs.python.org/3.14/library/math.html#math.ceil) function.

[Subject index](INDEX.md) · [Previous](fractions-fraction-class-to-fractions-fraction-class.md) · [Continue](fraction-numeric-protocol-and-changes.md) · [Owning module, declaration or section: fractions](fractions-fraction-class-to-fractions-fraction-class.md) · [Owning module, declaration or section: fractions.Fraction; fractions.Fraction; fractions.Fraction](fractions-fraction-class-to-fractions-fraction-class.md)
