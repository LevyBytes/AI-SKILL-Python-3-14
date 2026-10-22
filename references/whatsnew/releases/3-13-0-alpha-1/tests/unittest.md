# Python 3.13.0 alpha 1 / tests / unittest

[gh-104090](https://github.com/python/cpython/issues/104090): Steered clear of building a reference to the test object within [`collectedDurations()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult.collectedDurations).

[gh-89392](https://github.com/python/cpython/issues/89392): Took out support for the `test_main()` function across tests. They henceforth rely uniformly on the standard unittest test runner.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
