# Python 3.10.0 alpha 6 / library / concurrent futures

[bpo-40692](https://bugs.python.org/issue?@action=redirect&bpo=40692): Within [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), confirm that `multiprocess.synchronize()` exists on the platform at hand, and use that check across the [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) test suite so that tests with no bearing on `ProcessPoolExecutor` can still run on such platforms.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
