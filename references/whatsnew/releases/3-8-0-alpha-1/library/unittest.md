# Python 3.8.0 alpha 1 / library / unittest

[bpo-34318](https://bugs.python.org/issue?@action=redirect&bpo=34318): [`assertRaises()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaises), [`assertRaisesRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertRaisesRegex), [`assertWarns()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarns) and [`assertWarnsRegex()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertWarnsRegex) no longer succeed when the supplied callable is None. In context manager mode they no longer overlook unknown keyword arguments. Since Python 3.5 a DeprecationWarning had been raised in these situations.

[bpo-34900](https://bugs.python.org/issue?@action=redirect&bpo=34900): Corrected [`unittest.TestCase.debug()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.debug) when it is used to run test methods that contain subtests. Bruno Oliveira wrote the patch.

[bpo-24412](https://bugs.python.org/issue?@action=redirect&bpo=24412): unittest gained [`addModuleCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.addModuleCleanup) and [`addClassCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addClassCleanup) so that cleanups can run for [`setUpModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.setUpModule) and [`setUpClass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.setUpClass). Lisa Roach wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
