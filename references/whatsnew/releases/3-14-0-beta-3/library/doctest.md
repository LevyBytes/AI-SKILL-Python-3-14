# Python 3.14.0 beta 3 / library / doctest

[gh-134857](https://github.com/python/cpython/issues/134857): Error reporting for [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest)s executed under [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) was improved. `doctest` module frames are stripped from tracebacks, as is a redundant newline character from the failure message.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
