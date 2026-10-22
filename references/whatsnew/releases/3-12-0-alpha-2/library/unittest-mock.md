# Python 3.12.0 alpha 2 / library / unittest mock

[gh-91803](https://github.com/python/cpython/issues/91803): Resolve an error that surfaced when calling a method on objects mocked through [`unittest.mock.create_autospec()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.create_autospec) once they had been sealed by the [`unittest.mock.seal()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.seal) function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
