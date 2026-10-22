# Python 3.7.0 alpha 3 / library / time

[bpo-31784](https://bugs.python.org/issue?@action=redirect&bpo=31784): Following [**PEP 564**](https://peps.python.org/pep-0564/), six fresh functions delivering nanosecond precision were introduced into the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module: [`clock_gettime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime_ns), [`clock_settime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_settime_ns), [`monotonic_ns()`](https://docs.python.org/3.14/library/time.html#time.monotonic_ns), [`perf_counter_ns()`](https://docs.python.org/3.14/library/time.html#time.perf_counter_ns), [`process_time_ns()`](https://docs.python.org/3.14/library/time.html#time.process_time_ns), [`time_ns()`](https://docs.python.org/3.14/library/time.html#time.time_ns).

[bpo-31917](https://bugs.python.org/issue?@action=redirect&bpo=31917): Add 3 new clock identifiers: [`time.CLOCK_BOOTTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_BOOTTIME), [`time.CLOCK_PROF`](https://docs.python.org/3.14/library/time.html#time.CLOCK_PROF) and [`time.CLOCK_UPTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_UPTIME).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
