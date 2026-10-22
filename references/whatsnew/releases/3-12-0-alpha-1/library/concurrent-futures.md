# Python 3.12.0 alpha 1 / library / concurrent futures

[gh-95166](https://github.com/python/cpython/issues/95166): [`concurrent.futures.Executor.map()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map) is fixed so that the future presently being awaited is cancelled on an error - say TimeoutError or KeyboardInterrupt.

[gh-90622](https://github.com/python/cpython/issues/90622): Worker processes belonging to [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) are no longer created on demand (a capability that arrived in 3.9) whenever the multiprocessing context start method is `"fork"`, since forking while threads run can deadlock the child processes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
