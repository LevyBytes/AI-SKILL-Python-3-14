# time: `time.get_clock_info()`, `time.gmtime()`, `time.localtime()`, `time.mktime()`

time.get_clock_info(*name*)

Fetch details about the named clock packaged as a namespace object. These are the clock names that work and the matching functions that read their value:

- `'monotonic'`: `time.monotonic()`

- `'perf_counter'`: `time.perf_counter()`

- `'process_time'`: `time.process_time()`

- `'thread_time'`: `time.thread_time()`

- `'time'`: `time.time()`

These attributes accompany the result:

- *adjustable*: `True` when the clock can be made to leap forward or backward in time, otherwise `False`. This says nothing about gradual NTP rate adjustments.

- *implementation*: The name of the C function underneath that fetches the clock value. Possible values appear under Clock ID Constants.

- *monotonic*: `True` when the clock is unable to run backward, otherwise `False`

- *resolution*: How fine the clock's resolution is, in seconds ([`float`](https://docs.python.org/3.14/library/functions.html#float))

Added in version 3.3.

 time.gmtime([*secs*])

Take a time given as seconds since the epoch and turn it into a `struct_time` in UTC whose dst flag is forever zero. When *secs* is omitted or [`None`](https://docs.python.org/3.14/library/constants.html#None), what `time()` returns for the current time is used. Any fractional part of a second is discarded. The `struct_time` object is described above. The inverse of this function is [`calendar.timegm()`](https://docs.python.org/3.14/library/calendar.html#calendar.timegm).

 time.localtime([*secs*])

Behaves like `gmtime()` save that it converts to local time. When *secs* is omitted or [`None`](https://docs.python.org/3.14/library/constants.html#None), what `time()` returns for the current time is used. The dst flag becomes `1` whenever DST applies to the supplied time.

`localtime()` can raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when the timestamp falls outside the span of values the platform C `localtime()` or `gmtime()` functions handle, and [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) should `localtime()` or `gmtime()` fail. Frequently the practical limit here is years from 1970 through 2038.

 time.mktime(*t*)

This serves as the inverse of `localtime()`. What you pass is the `struct_time` or the full 9-tuple (the dst flag is required, so supply `-1` for the dst flag when you do not know it) conveying the time in *local* time as opposed to UTC. Back comes a floating-point number, keeping it compatible with `time()`. Should the supplied value not map to a valid time, either [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised (which one hinges on whether Python or the C libraries underneath catches the bad value). How far back in time it can produce a value is platform-dependent.

[Subject index](INDEX.md) · [Previous](time-asctime-to-time-ctime.md) · [Continue](functions.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
