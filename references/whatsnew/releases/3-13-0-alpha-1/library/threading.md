# Python 3.13.0 alpha 1 / library / threading

[gh-102029](https://github.com/python/cpython/issues/102029): Marked the passing of any arguments to [`threading.RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) as deprecated.

[gh-106236](https://github.com/python/cpython/issues/106236): Swap `assert` statements for `raise RuntimeError` within [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading), so that a `_DummyThread` resists being joined even under `-OO`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
