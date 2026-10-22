# Python 3.5.0 alpha 1 / library / tests and documentation

[bpo-22236](https://bugs.python.org/issue?@action=redirect&bpo=22236): The Tkinter tests no longer share the default root window. Each test class now gets a freshly created root window.

[bpo-15916](https://bugs.python.org/issue?@action=redirect&bpo=15916): Should it locate no tests, doctest.DocTestSuite now hands back an empty unittest.TestSuite in place of raising ValueError

[bpo-13223](https://bugs.python.org/issue?@action=redirect&bpo=13223): pydoc.writedoc was fixed so the HTML docs come out correctly for methods whose example code references ?self?.

[bpo-22894](https://bugs.python.org/issue?@action=redirect&bpo=22894): TestCase.subTest() had been halting the test suite under failfast mode even when nothing failed.

[bpo-21499](https://bugs.python.org/issue?@action=redirect&bpo=21499): Skip __builtins__ across a handful of test_importlib.test_api tests.

[bpo-21793](https://bugs.python.org/issue?@action=redirect&bpo=21793): The http.HTTPStatus enums were added (for example HTTPStatus.OK and HTTPStatus.NOT_FOUND). Demian Brecht supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
