# fractions: `fractions.Fraction`

## fractions — Rational numbers

### `fractions` — Rational numbers

**Source code:** [Lib/fractions.py](https://github.com/python/cpython/tree/3.14/Lib/fractions.py)

---

Arithmetic on rational numbers is what the `fractions` module backs.

You can build a Fraction instance out of two rational numbers, out of a lone number, or out of a string.

 *class *fractions.Fraction(*numerator=0*, *denominator=1*)

 *class *fractions.Fraction(*number*)

 *class *fractions.Fraction(*string*)

The opening version insists that *numerator* and *denominator* both be instances of [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational), and it yields a fresh `Fraction` instance whose value equals `numerator/denominator`. A zero *denominator* triggers a [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError).

The middle version insists that *number* be an instance of [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational) or carry the `as_integer_ratio()` method (which covers [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)). It yields a `Fraction` instance of precisely the same value. The presumption is that the `as_integer_ratio()` method gives back a coprime integer pair whose second member is positive. Bear in mind that, owing to the familiar binary-point pitfalls (consult [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html#tut-fp-issues)), the value handed to `Fraction(1.1)` doesn't precisely equal 11/10, so `Fraction(1.1)` does *not* hand back `Fraction(11, 10)` the way you might guess. (Though do look at the `limit_denominator()` method documented further down.)

The closing constructor version looks for a string. That instance typically takes the shape:

```python
[sign] numerator ['/' denominator]

```

in which the optional `sign` is either ‘+’ or ‘-’, while `numerator` and `denominator` (when given) are runs of decimal digits (and underscores may separate those digits, just as they do in integer literals within code). Beyond that, the `Fraction` constructor will take any string standing for a finite value that the [`float`](https://docs.python.org/3.14/library/functions.html#float) constructor would itself accept. With either shape, the input string is allowed leading and/or trailing whitespace too. A few examples follow:

```python
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)

```

Deriving from the abstract base class [`numbers.Rational`](https://docs.python.org/3.14/library/numbers.html#numbers.Rational), the `Fraction` class supplies every method and operation that class declares. A `Fraction` instance is [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) and ought to be regarded as immutable. On top of that, `Fraction` offers the properties and methods below:

Changed in version 3.2: The `Fraction` constructor began taking [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instances.

Changed in version 3.9: Normalizing the *numerator* and *denominator* now goes through the [`math.gcd()`](https://docs.python.org/3.14/library/math.html#math.gcd) function. Since `math.gcd()` always yields an [`int`](https://docs.python.org/3.14/library/functions.html#int) type, the GCD type is fixed; before, it hinged on *numerator* and *denominator*.

Changed in version 3.11: Building a `Fraction` instance from a string now allows underscores, in keeping with the [**PEP 515**](https://peps.python.org/pep-0515/) rules.

Changed in version 3.11: `Fraction` now provides `__int__`, which lets `typing.SupportsInt` instance checks pass.

Changed in version 3.12: A slash in string inputs may now be flanked by spaces: `Fraction('2 / 3')`.

Changed in version 3.12: A `Fraction` instance now accepts float-style formatting, covering the presentation types `"e"`, `"E"`, `"f"`, `"F"`, `"g"`, `"G"` and `"%""`.

Changed in version 3.13: When a `Fraction` instance is formatted with no presentation type, fill, alignment, sign handling, minimum width, and grouping are now honored.

Changed in version 3.14: The `Fraction` constructor now takes any object carrying the `as_integer_ratio()` method.

[Subject index](INDEX.md) · [Continue](fraction-construction-and-conversion.md)
