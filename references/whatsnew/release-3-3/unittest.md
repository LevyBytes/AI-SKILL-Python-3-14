# What's New In Python 3.3 / unittest — unittest

### unittest

When used as context managers, [`assertRaises()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaises), [`assertRaisesRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaisesRegex), [`assertWarns()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarns), and [`assertWarnsRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarnsRegex) henceforth take a *msg* keyword argument. Ezio Melotti and Winston Ewert contributed this ? see [bpo-10775](https://bugs.python.org/issue?@action=redirect&bpo=10775).

The [`TestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TestResult) object is now handed back by [`unittest.TestCase.run()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.run).

[Subject index](INDEX.md) · [Previous source section](types.md) · [Next source section](urllib.md) · [Release/subject declaration](summary-release-highlights.md)
