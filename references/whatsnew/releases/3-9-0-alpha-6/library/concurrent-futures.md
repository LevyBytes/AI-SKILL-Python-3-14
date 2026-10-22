# Python 3.9.0 alpha 6 / library / concurrent futures

[bpo-39812](https://bugs.python.org/issue?@action=redirect&bpo=39812): Daemon threads were taken out of [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures) by way of a new internal `threading._register_atexit()`, which runs the registered functions before any non-daemon threads are joined. The result is compatibility with subinterpreters, where daemon threads aren't supported.

[bpo-39207](https://bugs.python.org/issue?@action=redirect&bpo=39207): Within [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), workers are at this point created on demand, only where no free idle worker exists for reuse. This trims startup cost and cuts the CPU time wasted on idle workers. Kyle Stanley supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
