# Python 3.14.0 alpha 7 / library / threading

[gh-115942](https://github.com/python/cpython/issues/115942): Added [`threading.RLock.locked()`](https://docs.python.org/3.14/library/threading.html#threading.RLock.locked), [`multiprocessing.Lock.locked()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Lock.locked), [`multiprocessing.RLock.locked()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.RLock.locked), and made [`multiprocessing.managers.SyncManager.Lock()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.Lock) plus [`multiprocessing.managers.SyncManager.RLock()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.RLock) able to proxy the `locked()` call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
