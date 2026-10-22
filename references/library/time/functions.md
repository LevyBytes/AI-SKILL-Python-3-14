# time: Clock monotonicity, performance and CPU-time behavior

time.monotonic() — [float](https://docs.python.org/3.14/library/functions.html#float)

Hand back the value (in fractional seconds) of a monotonic clock — that is, one that is unable to run backwards. Updates to the system clock leave it untouched. Where the returned value's reference point sits is undefined, so only the gap between two calls' results carries meaning.

Clock:

- On Windows, call `QueryPerformanceCounter()` and `QueryPerformanceFrequency()`.

- On macOS, call `mach_absolute_time()` and `mach_timebase_info()`.

- On HP-UX, call `gethrtime()`.

- Call `clock_gettime(CLOCK_HIGHRES)` if available.

- Otherwise, call `clock_gettime(CLOCK_MONOTONIC)`.

Reach for `monotonic_ns()` so you sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type brings.

Added in version 3.3.

Changed in version 3.5: This function is available everywhere now, and every process shares the same clock.

Changed in version 3.10: Every process on macOS now shares the same clock.

 time.monotonic_ns() — [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `monotonic()`, but the time comes back in nanoseconds.

Added in version 3.7.

 time.perf_counter() — [float](https://docs.python.org/3.14/library/functions.html#float)

Hand back the value (in fractional seconds) of a performance counter — that is, a clock offering the finest resolution on hand for timing a brief stretch. Time spent sleeping is counted in. Every process shares this clock. Where the returned value's reference point sits is undefined, so only the gap between two calls' results carries meaning.

**CPython implementation detail:** Under CPython this draws on the same clock as `time.monotonic()` and is itself a monotonic clock — that is, one that is unable to run backwards.

Reach for `perf_counter_ns()` so you sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type brings.

Added in version 3.3.

Changed in version 3.10: Every process on Windows now shares the same clock.

Changed in version 3.13: Draws on the same clock as `time.monotonic()`.

 time.perf_counter_ns() — [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `perf_counter()`, but the time comes back in nanoseconds.

Added in version 3.7.

 time.process_time() — [float](https://docs.python.org/3.14/library/functions.html#float)

Hand back the value (in fractional seconds) representing the system plus user CPU time of the current process summed together. Time spent sleeping is left out. By its very nature it spans the whole process. Where the returned value's reference point sits is undefined, so only the gap between two calls' results carries meaning.

Reach for `process_time_ns()` so you sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type brings.

Added in version 3.3.

 time.process_time_ns() — [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `process_time()` but the time comes back in nanoseconds.

Added in version 3.7.

time.time() — [float](https://docs.python.org/3.14/library/functions.html#float)

Hand back the time in seconds since the epoch as a floating-point number. How [leap seconds](https://en.wikipedia.org/wiki/Leap_second) get handled rests on the platform. On Windows and the bulk of Unix systems, leap seconds do not count toward the time in seconds since the epoch. This is what people usually call [Unix time](https://en.wikipedia.org/wiki/Unix_time).

Bear in mind that, though the time always comes back as a floating-point number, not every system can supply time finer than 1 second. Although this function ordinarily yields non-decreasing values, it may return something smaller than an earlier call when the system clock has been moved back between the two calls.

You can turn the number `time()` gives back into a more familiar time format (year, month, day, hour, and so on) in UTC by handing it to the `gmtime()` function, or in local time by handing it to the `localtime()` function. Either way a `struct_time` object comes back, and from it the parts of the calendar date are reachable as attributes.

Clock:

- On Windows, call `GetSystemTimePreciseAsFileTime()`.

- Call `clock_gettime(CLOCK_REALTIME)` if available.

- Otherwise, call `gettimeofday()`.

[Subject index](INDEX.md) · [Previous](time-get-clock-info-to-time-mktime.md) · [Continue](time-sleep.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md) · [Previous](time-struct-time-class.md) · [Required continuation of the source contract](time-tzset.md)
