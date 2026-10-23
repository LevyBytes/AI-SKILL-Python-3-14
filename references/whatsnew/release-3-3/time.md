# What's New In Python 3.3 / time - time

### time

These functions were introduced into the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module by [**PEP 418**](https://peps.python.org/pep-0418/):

- [`get_clock_info()`](https://docs.python.org/3.14/library/time.html#time.get_clock_info): Get information on a clock.

- [`monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic): Monotonic clock (cannot go backward), not affected by system clock updates.

- [`perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter): Performance counter with the highest available resolution to measure a short duration.

- [`process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time): Sum of the system and user CPU time of the current process.

Further new functions:

- [`clock_getres()`](https://docs.python.org/3.14/library/time.html#time.clock_getres), [`clock_gettime()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime) and [`clock_settime()`](https://docs.python.org/3.14/library/time.html#time.clock_settime) functions with `CLOCK_*xxx*` constants. Victor Stinner contributed these ? see [bpo-10278](https://bugs.python.org/issue?@action=redirect&bpo=10278).

For better consistency across platforms, [`sleep()`](https://docs.python.org/3.14/library/time.html#time.sleep) henceforth throws a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) if handed a negative duration. That was formerly a posix error, yet on Windows it would sleep forever.

[Subject index](INDEX.md) · [Previous source section](threading.md) · [Next source section](types.md) · [Release/subject declaration](summary-release-highlights.md)
