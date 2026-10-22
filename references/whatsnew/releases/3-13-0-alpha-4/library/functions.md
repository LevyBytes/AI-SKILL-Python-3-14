# Python 3.13.0 alpha 4 / library / functions

[gh-114563](https://github.com/python/cpython/issues/114563): Repair several [`format()`](https://docs.python.org/3.14/library/functions.html#format) defects affecting the C implementation of [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal): * a memory leak that appears in rare cases under the `z` format option (coerce negative 0) * wrong output when the `z` format option is applied to type `F` (fixed-point with capital `NAN` / `INF`) * wrong output when the `#` format option (alternate form) is applied

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
