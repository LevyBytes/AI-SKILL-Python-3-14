# Python 3.13.0 alpha 5 / library / time

[gh-115714](https://github.com/python/cpython/issues/115714): On WASI, the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module no longer pulls process time out of `times()` or `CLOCK_PROCESS_CPUTIME_ID`; that system API is unreliable and stands to be dropped from WASI. The clock functions affected drop back to calling `clock()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
