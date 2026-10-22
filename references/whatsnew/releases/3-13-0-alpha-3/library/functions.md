# Python 3.13.0 alpha 3 / library / functions

[gh-112345](https://github.com/python/cpython/issues/112345): Provide a clearer error message when [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) is called against a [`typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol) whose members are not all methods. Randolf Scholz wrote the patch.

[gh-74690](https://github.com/python/cpython/issues/74690): Make [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) tests against plain [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) roughly 6% quicker. Alex Waygood wrote the patch.

[gh-112414](https://github.com/python/cpython/issues/112414): Fix a Python 3.12 regression where invoking [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) on a module imported through a custom [loader](https://docs.python.org/3.14/glossary.html#term-loader) could break with [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). Alex Waygood wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
