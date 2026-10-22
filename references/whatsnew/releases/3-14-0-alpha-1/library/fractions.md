# Python 3.14.0 alpha 1 / library / fractions

[gh-121797](https://github.com/python/cpython/issues/121797): Provide a second [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) constructor named [`Fraction.from_number()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.from_number).

[gh-119838](https://github.com/python/cpython/issues/119838): For mixed arithmetic that combines a [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) with a complex, the fraction is henceforth promoted to [`float`](https://docs.python.org/3.14/library/functions.html#float) rather than [`complex`](https://docs.python.org/3.14/library/functions.html#complex).

[gh-82017](https://github.com/python/cpython/issues/82017): Conversion to a [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) is now possible for any object that exposes an `as_integer_ratio()` method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
