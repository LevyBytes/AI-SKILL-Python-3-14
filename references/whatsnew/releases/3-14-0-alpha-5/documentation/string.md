# Python 3.14.0 alpha 5 / documentation / string

[gh-67206](https://github.com/python/cpython/issues/67206): Note that [`string.printable`](https://docs.python.org/3.14/library/string.html#string.printable) is not printable in the POSIX sense. Specifically, [`string.printable.isprintable()`](https://docs.python.org/3.14/library/stdtypes.html#str.isprintable) yields [`False`](https://docs.python.org/3.14/library/constants.html#False). Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
