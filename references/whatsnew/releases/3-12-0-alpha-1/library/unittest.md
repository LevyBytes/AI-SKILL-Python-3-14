# Python 3.12.0 alpha 1 / library / unittest

[gh-95736](https://github.com/python/cpython/issues/95736): [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase) is corrected so the event loop is established ahead of running setup functions. Kumar Aditya wrote the patch.

[gh-89325](https://github.com/python/cpython/issues/89325): Cleared out a host of long-deprecated [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) features: the [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) method aliases, the undocumented and broken `TestCase` method `assertDictContainsSubset`, the undocumented *use_load_tests* parameter on [`TestLoader.loadTestsFromModule`](https://docs.python.org/3.14/library/unittest.html#unittest.TestLoader.loadTestsFromModule), and an underscore-prefixed alias for the [`TextTestResult`](https://docs.python.org/3.14/library/unittest.html#unittest.TextTestResult) class.

[gh-93096](https://github.com/python/cpython/issues/93096): The undocumented `python -m codecs` is removed. Run `python -m unittest test.test_codecs.EncodedFileTest` in its place.

[gh-93096](https://github.com/python/cpython/issues/93096): The undocumented `-t` argument belonging to `python -m base64` is removed. Run `python -m unittest test.test_base64.LegacyBase64TestCase.test_encodebytes` in its place.

[gh-97837](https://github.com/python/cpython/issues/97837): Updates the deprecation warning text in [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest), replacing

`It is deprecated to return a value!=None`

with

`It is deprecated to return a value that is not None from a test case`

[bpo-45046](https://bugs.python.org/issue?@action=redirect&bpo=45046): Added context-manager support to [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest): the [`enterContext()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.enterContext) and [`enterClassContext()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.enterClassContext) methods on the [`TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase) class, the [`enterAsyncContext()`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase.enterAsyncContext) method on the [`IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase) class, and the [`unittest.enterModuleContext()`](https://docs.python.org/3.14/library/unittest.html#unittest.enterModuleContext) function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
