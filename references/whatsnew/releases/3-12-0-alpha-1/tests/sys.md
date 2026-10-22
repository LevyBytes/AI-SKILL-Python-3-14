# Python 3.12.0 alpha 1 / tests / sys

[gh-93575](https://github.com/python/cpython/issues/93575): Address the test_unicode test_raiseMemError problem. That test case now relies on `test.support.calcobjsize` to compute the size of PyUnicode structs. [`sys.getsizeof()`](https://docs.python.org/3.14/library/sys.html#sys.getsizeof) can report a different size once a string holds UTF-8 memory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
