# Python 3.14.0 alpha 3 / c api / threads and concurrency

[gh-121058](https://github.com/python/cpython/issues/121058): Whenever the thread state still carries an active exception, `PyThreadState_Clear()` now emits a warning and invokes `sys.excepthook`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
