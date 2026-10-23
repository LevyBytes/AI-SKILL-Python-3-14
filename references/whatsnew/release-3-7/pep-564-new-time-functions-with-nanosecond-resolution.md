# What's New In Python 3.7 / PEP 564: New Time Functions With Nanosecond Resolution - time

### PEP 564: New Time Functions With Nanosecond Resolution

On today's machines, clock resolution can outstrip the bounded precision of the floating-point value handed back by the [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) function and its relatives. So that precision isn't lost, [**PEP 564**](https://peps.python.org/pep-0564/) introduces six fresh "nanosecond" counterparts of the current timer functions in the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module:

- [`time.clock_gettime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_gettime_ns)

- [`time.clock_settime_ns()`](https://docs.python.org/3.14/library/time.html#time.clock_settime_ns)

- [`time.monotonic_ns()`](https://docs.python.org/3.14/library/time.html#time.monotonic_ns)

- [`time.perf_counter_ns()`](https://docs.python.org/3.14/library/time.html#time.perf_counter_ns)

- [`time.process_time_ns()`](https://docs.python.org/3.14/library/time.html#time.process_time_ns)

- [`time.time_ns()`](https://docs.python.org/3.14/library/time.html#time.time_ns)

These new functions hand back a nanosecond count as an integer.

[**Measurements**](https://peps.python.org/pep-0564/#annex-clocks-resolution-in-python) indicate that under Linux and Windows the resolution of [`time.time_ns()`](https://docs.python.org/3.14/library/time.html#time.time_ns) runs roughly 3 times finer than [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time).

See also

[**PEP 564**](https://peps.python.org/pep-0564/): Add new time functions with nanosecond resolution

PEP written and implemented by Victor Stinner

[Subject index](INDEX.md) · [Previous source section](pep-562-customization-of-access-to-module-attributes.md) · [Next source section](pep-565-show-deprecationwarning-in-main.md) · [Release/subject declaration](summary-release-highlights.md)
