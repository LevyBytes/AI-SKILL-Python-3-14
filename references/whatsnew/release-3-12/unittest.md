# What’s New In Python 3.12 / unittest

### unittest

A `--durations` command line option is now available; it surfaces the N test cases that ran the slowest:

```python
python3 -m unittest --durations=3 lib.tests.test_threading
.....
Slowest test durations
----------------------------------------------------------------------
1.210s     test_timeout (Lib.test.test_threading.BarrierTests)
1.003s     test_default_timeout (Lib.test.test_threading.BarrierTests)
0.518s     test_timeout (Lib.test.test_threading.EventTests)

(0.000 durations hidden.  Use -v to show these durations.)
----------------------------------------------------------------------
Ran 158 tests in 9.869s

OK (skipped=3)

```

(Contributed by Giampaolo Rodola in [gh-48330](https://github.com/python/cpython/issues/48330))

### unittest

- Drop a host of [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) features deprecated long ago:

  - A number of [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) method aliases:

| Deprecated alias | Method Name | Deprecated in |
| --- | --- | --- |
| `failUnless` | `assertTrue()` | 3.1 |
| `failIf` | `assertFalse()` | 3.1 |
| `failUnlessEqual` | `assertEqual()` | 3.1 |
| `failIfEqual` | `assertNotEqual()` | 3.1 |
| `failUnlessAlmostEqual` | `assertAlmostEqual()` | 3.1 |
| `failIfAlmostEqual` | `assertNotAlmostEqual()` | 3.1 |
| `failUnlessRaises` | `assertRaises()` | 3.1 |
| `assert_` | `assertTrue()` | 3.2 |
| `assertEquals` | `assertEqual()` | 3.2 |
| `assertNotEquals` | `assertNotEqual()` | 3.2 |
| `assertAlmostEquals` | `assertAlmostEqual()` | 3.2 |
| `assertNotAlmostEquals` | `assertNotAlmostEqual()` | 3.2 |
| `assertRegexpMatches` | `assertRegex()` | 3.2 |
| `assertRaisesRegexp` | `assertRaisesRegex()` | 3.2 |
| `assertNotRegexpMatches` | `assertNotRegex()` | 3.5 |

To migrate your unit tests automatically, the tool at [https://github.com/isidentical/teyit](https://github.com/isidentical/teyit) handles the modernisation for you.

  - The undocumented and non-working [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) method named `assertDictContainsSubset` (which had been deprecated back in Python 3.2).

  - The undocumented *use_load_tests* parameter on [`TestLoader.loadTestsFromModule`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule) (deprecated, and disregarded, ever since Python 3.5).

  - The `_TextTestResult` name, which aliased the [`TextTestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TextTestResult) class (deprecated as of Python 3.2).

(Contributed by Serhiy Storchaka in [gh-89325](https://github.com/python/cpython/issues/89325).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](uuid.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](ssl.md) · [Next source section](webbrowser.md)
