# time: `time.asctime()`, `time.pthread_getcpuclockid()`, `time.clock_getres()`, `time.clock_settime()`, `time.clock_settime_ns()`, `time.ctime()`

### Functions

 time.asctime([*t*])

Take a tuple or `struct_time` standing for a time of the kind `gmtime()` or `localtime()` produces and turn it into a string shaped like this: `'Sun Jun 20 23:21:05 1993'`. Two characters wide, the day field gets space padding whenever the day is a single digit, for example: `'Wed Jun 9 04:26:40 1993'`.

When *t* is omitted, what `localtime()` returns for the current time is used. `asctime()` pays no attention to locale information.

Note

In contrast to the C function it shares a name with, `asctime()` tacks on no trailing newline.

 time.pthread_getcpuclockid(*thread_id*)

Hand back the *clk_id* belonging to the thread-specific CPU-time clock for the given *thread_id*.

To obtain a value suitable for *thread_id*, reach for [`threading.get_ident()`](https://docs.python.org/3.14/library/threading.html#threading.get_ident) or the [`ident`](https://docs.python.org/3.14/library/threading.html#threading.Thread.ident) attribute carried by [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) objects.

Warning

Handing over a *thread_id* that is invalid or has expired can trigger undefined behavior, segmentation fault among the possibilities.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix

For more detail, check the man page for *[pthread_getcpuclockid(3)](https://manpages.debian.org/pthread_getcpuclockid(3))*.

Added in version 3.7.

 time.clock_getres(*clk_id*)

Give back how fine the resolution (precision) of the named clock *clk_id* is. The accepted values for *clk_id* are catalogued under Clock ID Constants.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 time.clock_gettime(*clk_id*) — [float](https://docs.python.org/3.14/library/functions.html#float)

Give back the time held by the named clock *clk_id*. The accepted values for *clk_id* are catalogued under Clock ID Constants.

Reach for `clock_gettime_ns()` so you sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type brings.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 time.clock_gettime_ns(*clk_id*) — [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `clock_gettime()` except the time comes back in nanoseconds.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.7.

 time.clock_settime(*clk_id*, *time: [float](https://docs.python.org/3.14/library/functions.html#float)*)

Assign the time held by the named clock *clk_id*. At present `CLOCK_REALTIME` is the sole accepted value for *clk_id*.

Reach for `clock_settime_ns()` so you sidestep the precision loss that the [`float`](https://docs.python.org/3.14/library/functions.html#float) type brings.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not Android, not iOS.

Added in version 3.3.

 time.clock_settime_ns(*clk_id*, *time: [int](https://docs.python.org/3.14/library/functions.html#int)*)

Behaves like `clock_settime()` except you set the time in nanoseconds.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not Android, not iOS.

Added in version 3.7.

 time.ctime([*secs*])

Take a time given as seconds since the epoch and render it into a string of the form `'Sun Jun 20 23:21:05 1993'` standing for local time. Two characters wide, the day field gets space padding whenever the day is a single digit, for example: `'Wed Jun 9 04:26:40 1993'`.

When *secs* is omitted or [`None`](https://docs.python.org/3.14/library/constants.html#None), what `time()` returns for the current time is used. Calling `ctime(secs)` amounts to `asctime(localtime(secs))`. `ctime()` pays no attention to locale information.

[Subject index](INDEX.md) · [Previous](time-time-access-and-conversions.md) · [Continue](time-get-clock-info-to-time-mktime.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md)
