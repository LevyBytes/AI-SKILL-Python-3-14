# Python 3.8.0 alpha 1 / library / time

[bpo-34054](https://bugs.python.org/issue?@action=redirect&bpo=34054): For implementing timeouts, the multiprocessing module now reads the monotonic clock [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) rather than the system clock [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time).

[bpo-35702](https://bugs.python.org/issue?@action=redirect&bpo=35702): The [`time.CLOCK_UPTIME_RAW`](https://docs.python.org/3.14/library/time.html#time.CLOCK_UPTIME_RAW) constant can now be used on macOS 10.12.

[bpo-35513](https://bugs.python.org/issue?@action=redirect&bpo=35513): The `TextTestRunner` from `unittest.runner` now relies on [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) rather than [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) when timing a test run: `time.time()` may move backwards, while `time.perf_counter()` keeps increasing monotonically.

[bpo-34672](https://bugs.python.org/issue?@action=redirect&bpo=34672): Added a workaround so that, in certain situations, the `'Z'` [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) specifier functions on the musl C library.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
