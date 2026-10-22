# Python 3.14.0 beta 3 / library / concurrent futures

[gh-132969](https://github.com/python/cpython/issues/132969): The [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) executor thread, which keeps running after [`shutdown(wait=False)`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.shutdown), is now prevented from trying to rebalance the pool’s worker processes once the object state was already reset during shutdown. Several conditions together — among them a worker process that ended abormally — produced an exception plus a possible hang while the still-running executor thread tried to swap dead workers inside the pool.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
