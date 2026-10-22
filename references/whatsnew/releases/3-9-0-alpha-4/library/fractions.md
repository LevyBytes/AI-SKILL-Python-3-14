# Python 3.9.0 alpha 4 / library / fractions

[bpo-39350](https://bugs.python.org/issue?@action=redirect&bpo=39350): Fix a regression in [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) when the numerator and/or the denominator is an [`int`](https://docs.python.org/3.14/library/functions.html#int) subclass. The [`math.gcd()`](https://docs.python.org/3.14/library/math.html#math.gcd) function now handles normalizing the *numerator* and *denominator*. `math.gcd()` always return a `int` type. Beforehand, the GCD type was governed by *numerator* and *denominator*.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
