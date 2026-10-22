# Python 3.12.0 beta 1 / library / unittest

[gh-68968](https://github.com/python/cpython/issues/68968): Corrected the scrambled rendering from [`assertEqual()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual) whenever an input is missing its closing newline.

[gh-62432](https://github.com/python/cpython/issues/62432): Should no tests run, the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) runner now exits with status code 5. A misconfigured test runner often turns up no tests at all, and that ought to count as an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
