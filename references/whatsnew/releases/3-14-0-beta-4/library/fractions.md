# Python 3.14.0 beta 4 / library / fractions

[gh-130662](https://github.com/python/cpython/issues/130662): For [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) formatting, leading zeros are now accepted within the precision and width fields; one example is `format(Fraction(1, 3), '.016f')`.

[gh-87790](https://github.com/python/cpython/issues/87790): Within the fractional part of [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)’s formatting, underscore and comma are now supported as thousands separators. Sergey B Kirpichev authored this patch.

[gh-130664](https://github.com/python/cpython/issues/130664): A corner-case for [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)’s formatting is now handled: zero-padding (prefixing the width field with a zero (`'0'`) character) is treated the same as a fill character of `'0'` paired with an alignment type of `'='`, exactly as is done for [`float`](https://docs.python.org/3.14/library/functions.html#float)’s.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
