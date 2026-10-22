# Python 3.13.0 alpha 1 / library / datetime

[gh-109495](https://github.com/python/cpython/issues/109495): Drop a redundant extra `__slots__` from the pure python implementation of [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), reducing memory size, since the superclass already defines them. James Hilton-Balfe wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
