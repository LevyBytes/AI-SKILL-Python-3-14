# Python 3.9.0 alpha 6 / library / unittest mock

[bpo-40126](https://bugs.python.org/issue?@action=redirect&bpo=40126): Reverting several patches at once in unittest.mock is now fixed. A patcher's `__exit__()` will no longer run whenever its `__enter__()` failed. The exception is now suppressed when `__exit__()` returns true.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
