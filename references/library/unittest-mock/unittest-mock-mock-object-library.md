# unittest.mock`unittest.mock` - mock object library

### `unittest.mock` - mock object library

Added in version 3.3.

**Source code:** [Lib/unittest/mock.py](https://github.com/python/cpython/tree/3.14/Lib/unittest/mock.py)

---

For testing purposes in Python, `unittest.mock` is the supplied library. With it you can swap out portions of the system being exercised for mock objects and then assert against the manner in which those objects were exercised.

At its heart, `unittest.mock` supplies a `Mock` class that spares you from writing numerous stubs scattered across your tests. Once an operation runs, you are free to assert which attributes or methods got touched and with what arguments they were invoked. Return values can be declared and any required attributes assigned in the usual fashion as well.

On top of that, the library offers a `patch()` decorator that takes care of patching attributes at the module and class level only for the duration of a test, plus `sentinel` for minting one-of-a-kind objects. The quick guide below walks through several examples covering `Mock`, `MagicMock` and `patch()`.

Built to pair with [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest), Mock follows the ‘action -> assertion’ approach rather than the ‘record -> replay’ style adopted by a number of other mocking frameworks.

For older Python releases there is a backport of `unittest.mock`, distributed as [mock](https://pypi.org/project/mock/) on PyPI.

[Subject index](INDEX.md) · [Continue](quick-guide-section-introduction-and-initial-examples.md)
