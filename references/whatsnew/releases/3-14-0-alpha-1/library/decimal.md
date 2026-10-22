# Python 3.14.0 alpha 1 / library / decimal

[gh-123657](https://github.com/python/cpython/issues/123657): Repairs a crash plus memory leak in [`decimal.getcontext()`](https://docs.python.org/3.14/library/decimal.html#decimal.getcontext). The crash showed up with a thread-local context built via `--with-decimal-contextvar=no`.

[gh-121798](https://github.com/python/cpython/issues/121798): Provide a second [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) constructor named [`Decimal.from_number()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.from_number).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
