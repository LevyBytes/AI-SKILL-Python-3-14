# Python 3.14.0 alpha 2 / library / multiprocessing

[gh-126417](https://github.com/python/cpython/issues/126417): The `multiprocessing.managers.DictProxy` and `multiprocessing.managers.ListProxy` types from [`multiprocessing.managers`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing.managers) are now registered against [`collections.abc.MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping) and [`collections.abc.MutableSequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableSequence), in that order.

[gh-71936](https://github.com/python/cpython/issues/71936): Repair a race condition within [`multiprocessing.pool.Pool`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool).

[gh-117378](https://github.com/python/cpython/issues/117378): Correct the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) `"forkserver"` start method so its forkserver process properly picks up the parent’s [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) while importing the [`multiprocessing.set_forkserver_preload()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.set_forkserver_preload) modules, matching the way `sys.path` gets set up in workers before they run work items.

Because of this bug, certain forkserver module preloading would quietly fail to preload. The symptom was slower child processes whenever `sys.path` was needed, owing to the extra repeated work each worker had to do.

Another possible side effect: `""` could linger in [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) throughout forkserver preload imports, in place of the absolute path taken from [`os.getcwd()`](https://docs.python.org/3.14/library/os.html#os.getcwd) at multiprocessing import time that the worker `sys.path` relies on.

Those between-phase `sys.path` discrepancies in the child process could in theory have led preload to pull in the wrong things from a wrong location. We have no knowledge of that ever occurring for real.

[gh-125679](https://github.com/python/cpython/issues/125679): On macOS, the `repr` of [`multiprocessing.Lock`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.Lock) and [`multiprocessing.RLock`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.RLock) no longer reports “unknown”.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
