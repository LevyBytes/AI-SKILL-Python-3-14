# Python 3.7.0 alpha 2 / library / concurrent futures

[bpo-31540](https://bugs.python.org/issue?@action=redirect&bpo=31540): Permit handing a context object to the [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) constructor. Job resources within `concurrent.futures.ProcessPoolExecutor` are also released sooner, improving memory usage while a worker awaits fresh jobs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
