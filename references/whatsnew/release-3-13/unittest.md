# What's New In Python 3.13 / unittest - unittest

### unittest

- Drop the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) functions listed below, all deprecated in Python 3.11:

  - `unittest.findTestCases()`

  - `unittest.makeSuite()`

  - `unittest.getTestCaseNames()`

Reach for [`TestLoader`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader) methods in their place:

  - [`loadTestsFromModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule)

  - [`loadTestsFromTestCase()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase)

  - [`getTestCaseNames()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.getTestCaseNames)

(Contributed by Hugo van Kemenade in [gh-104835](https://github.com/python/cpython/issues/104835).)

- Drop the untested and undocumented `TestProgram.usageExit()` method, which carried a Python 3.11 deprecation. (Contributed by Hugo van Kemenade in [gh-104992](https://github.com/python/cpython/issues/104992).)

[Subject index](INDEX.md) · [Previous source section](typing.md) · [Next source section](urllib.md) · [Release/subject declaration](summary-release-highlights.md)
