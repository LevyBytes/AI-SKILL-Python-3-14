# Python 3.12.0 beta 1 / library / unittest mock

[gh-102978](https://github.com/python/cpython/issues/102978): Corrects [`unittest.mock.patch()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch) so it enforces function signatures on methods carrying `@classmethod` or `@staticmethod` whenever patch runs with `autospec=True`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
