# Python 3.13.0 alpha 1 / library / decimal

[gh-89902](https://github.com/python/cpython/issues/89902): Mark the non-standard format specifier “N” for [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) as deprecated. That specifier had no documentation and worked only under the C implementation.

[gh-105375](https://github.com/python/cpython/issues/105375): Address a bug within [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) where an exception could wind up being overwritten.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
