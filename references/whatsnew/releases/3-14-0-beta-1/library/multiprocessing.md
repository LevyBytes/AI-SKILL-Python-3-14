# Python 3.14.0 beta 1 / library / multiprocessing

[gh-132561](https://github.com/python/cpython/issues/132561): Repair the public `locked` method on the `multiprocessing.SemLock` class. Also add 2 tests covering the derived [`multiprocessing.Lock`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Lock) and [`multiprocessing.RLock`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.RLock) classes.

[gh-131913](https://github.com/python/cpython/issues/131913): Provide a convenience function [`multiprocessing.Process.interrupt()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.interrupt) next to the present [`multiprocessing.Process.terminate()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.terminate) and [`multiprocessing.Process.kill()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Process.kill) so that child-process termination can be controlled more finely.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
