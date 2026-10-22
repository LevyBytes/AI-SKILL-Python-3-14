# Python 3.12.0 alpha 2 / tests / typing

[gh-98713](https://github.com/python/cpython/issues/98713): Correct a defect among the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) tests where one test that depended on CPython-specific internals lacked the `@cpython_only` decorator and therefore never got skipped on other implementations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
