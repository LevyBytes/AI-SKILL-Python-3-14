# Python 3.13.0 alpha 1 / library / unittest

[gh-104835](https://github.com/python/cpython/issues/104835): Deleted the following [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) functions, all deprecated back in Python 3.11:

  - `unittest.findTestCases()`

  - `unittest.makeSuite()`

  - `unittest.getTestCaseNames()`

Reach for [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) methods as replacements:

  - [`unittest.TestLoader.loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule)

  - [`unittest.TestLoader.loadTestsFromTestCase()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase)

  - [`unittest.TestLoader.getTestCaseNames()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.getTestCaseNames)

Hugo van Kemenade authored the change.

[gh-84867](https://github.com/python/cpython/issues/84867): [`unittest.TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) will no longer pull test cases out of the exact [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) and [`unittest.FunctionTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.FunctionTestCase) classes.

[gh-106584](https://github.com/python/cpython/issues/106584): Repair the `unittest` exit code for when every test is skipped. Egor Eliseev provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
