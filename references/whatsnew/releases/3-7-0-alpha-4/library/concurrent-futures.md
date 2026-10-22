# Python 3.7.0 alpha 4 / library / concurrent futures

[bpo-31699](https://bugs.python.org/issue?@action=redirect&bpo=31699): Resolves hangs in [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) triggered whenever a task's arguments or its results raise pickling or unpickling failures. With the fix, every call into the `ProcessPoolExecutor` API is guaranteed to return at some point.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
