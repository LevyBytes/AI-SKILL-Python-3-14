# Python 3.14.0 alpha 5 / c api / decimal

[gh-127925](https://github.com/python/cpython/issues/127925): Switched the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module over to the [**PEP 757**](https://peps.python.org/pep-0757/) C API (export-import integers), which speeds things up a little whenever a [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instance has a small integer part. Sergey B Kirpichev wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
