# Python 3.14.0 alpha 2 / library / threading

[gh-125541](https://github.com/python/cpython/issues/125541): Hitting Ctrl-C during a block in [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire), [`threading.RLock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.RLock.acquire), together with [`threading.Thread.join()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join) now breaks out of the call and throws a [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception under Windows, mirroring the behaviour those functions already show on macOS and Linux.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
