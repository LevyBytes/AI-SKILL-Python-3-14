# Python 3.13.0 beta 1 / core and builtins / decimal

[gh-118164](https://github.com/python/cpython/issues/118164): Sever a loop between the Python rendering of the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module and the Python routine handling integer-to-string conversion. Also tune integer-to-string conversion for values spanning 9_000 up to 135_000 decimal digits.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
