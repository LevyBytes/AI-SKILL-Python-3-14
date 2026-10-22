# Python 3.12.0 alpha 7 / library / unittest

[gh-48330](https://github.com/python/cpython/issues/48330): A `--durations` command line option that lists the N slowest test cases was added. The [`unittest.TextTestRunner`](https://docs.python.org/3.14/library/unittest.html#unittest.TextTestRunner) and [`unittest.TextTestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TextTestResult) constructors now take a fresh *durations* keyword argument. Any subclass should either account for this or accept `**kwargs`. A new [`unittest.TestResult.addDuration()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.addDuration) method plus a [`unittest.TestResult.collectedDurations`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.collectedDurations) attribute were also introduced.

(Giampaolo Rodola contributed this)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
