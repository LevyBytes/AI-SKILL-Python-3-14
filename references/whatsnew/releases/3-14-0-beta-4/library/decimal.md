# Python 3.14.0 beta 4 / library / decimal

[gh-130662](https://github.com/python/cpython/issues/130662): For [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) formatting, leading zeros are now accepted within the precision and width fields; one example is `format(Decimal(1.25), '.016f')`.

[gh-87790](https://github.com/python/cpython/issues/87790): Within the fractional part of [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal)’s formatting, underscore and comma are now supported as thousands separators. Sergey B Kirpichev authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
