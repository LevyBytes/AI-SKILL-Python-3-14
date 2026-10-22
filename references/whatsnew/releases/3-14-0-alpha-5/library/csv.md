# Python 3.14.0 alpha 5 / library / csv

[gh-129409](https://github.com/python/cpython/issues/129409): Repair an integer overflow in the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module that occurred when emitting any single data field above 2GB.

[gh-118761](https://github.com/python/cpython/issues/118761): Make importing [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) up to five times cheaper by loading [`re`](https://docs.python.org/3.14/library/re.html#module-re) only on demand. Consequently, `re` is no more implicitly exposed as `csv.re`. Bénédikt Tran contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
