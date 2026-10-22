# Python 3.9.0 alpha 4 / library / concurrent futures

[bpo-39349](https://bugs.python.org/issue?@action=redirect&bpo=39349): Introduced a fresh *cancel_futures* parameter on [`concurrent.futures.Executor.shutdown()`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.shutdown); it cancels every pending future not yet started rather than awaiting their completion ahead of shutting the executor down.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
