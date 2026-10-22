# Python 3.12.0 alpha 4 / library / fractions

[gh-91851](https://github.com/python/cpython/issues/91851): Tiny speedups for [`fractions.Fraction.__round__()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.__round__), [`fractions.Fraction.__ceil__()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.__ceil__) and [`fractions.Fraction.__floor__()`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction.__floor__).

[gh-100488](https://github.com/python/cpython/issues/100488): Add `Fraction.is_integer()` to test whether a [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) holds an integer. This brings duck-typing parity with [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`int`](https://docs.python.org/3.14/library/functions.html#int).

[gh-91851](https://github.com/python/cpython/issues/91851): Tune the [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) arithmetic for small components.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
