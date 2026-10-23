# What's New In Python 3.7 / time - time

### time

The [`time`](https://docs.python.org/3.14/library/time.html#module-time) module gains six fresh functions offering nanosecond resolution, courtesy of [**PEP 564**](https://peps.python.org/pep-0564/):

- [`time.clock_gettime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime_ns)

- [`time.clock_settime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_settime_ns)

- [`time.monotonic_ns()`](https://docs.python.org/3.14/library/time.html#time.monotonic_ns)

- [`time.perf_counter_ns()`](https://docs.python.org/3.14/library/time.html#time.perf_counter_ns)

- [`time.process_time_ns()`](https://docs.python.org/3.14/library/time.html#time.process_time_ns)

- [`time.time_ns()`](https://docs.python.org/3.14/library/time.html#time.time_ns)

Several additional clock identifiers are now provided:

- [`time.CLOCK_BOOTTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_BOOTTIME) (Linux): Matches [`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC), but additionally counts any interval during which the system is suspended.

- [`time.CLOCK_PROF`](https://docs.python.org/3.14/library/time.html#time.CLOCK_PROF) (FreeBSD, NetBSD and OpenBSD): High-resolution per-process CPU timer.

- [`time.CLOCK_UPTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_UPTIME) (FreeBSD, OpenBSD): A clock whose absolute reading equals how long the machine has run without being suspended, yielding an accurate uptime figure.

For per-thread CPU time readings, the freshly added [`time.thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) and [`time.thread_time_ns()`](https://docs.python.org/3.14/library/time.html#time.thread_time_ns) functions are available. (Contributed by Antoine Pitrou in [bpo-32025](https://bugs.python.org/issue?@action=redirect&bpo=32025).)

The thread-specific CPU-time clock's clock ID is reported by the freshly added [`time.pthread_getcpuclockid()`](https://docs.python.org/3.14/library/time.html#time.pthread_getcpuclockid) function.

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)
