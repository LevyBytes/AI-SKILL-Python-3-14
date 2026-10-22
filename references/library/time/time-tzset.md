# time: `time.tzset()`

Reach for `time_ns()` when you want to sidestep the loss of precision introduced by the [`float`](https://docs.python.org/3.14/library/functions.html#float) type.

Changed in version 3.13: On Windows, this now invokes `GetSystemTimePreciseAsFileTime()` rather than `GetSystemTimeAsFileTime()`.

 time.time_ns() → [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `time()`, though the result is delivered as a whole-number count of nanoseconds measured from the epoch.

Added in version 3.7.

 time.thread_time() → [float](https://docs.python.org/3.14/library/functions.html#float)

Hands back, in fractional seconds, the combined system and user CPU time charged to the calling thread. Spans spent asleep are not folded into this figure. The measurement is, by its very nature, particular to one thread. Since the origin of the returned figure is left unspecified, the only meaningful quantity is the gap between two separate readings taken inside the same thread.

Reach for `thread_time_ns()` when you want to sidestep the loss of precision introduced by the [`float`](https://docs.python.org/3.14/library/functions.html#float) type.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux, Unix, Windows.

Unix systems supporting `CLOCK_THREAD_CPUTIME_ID`.

Added in version 3.7.

 time.thread_time_ns() → [int](https://docs.python.org/3.14/library/functions.html#int)

Behaves like `thread_time()`, except the time is reported in nanoseconds.

Added in version 3.7.

 time.tzset()

Reloads the time-conversion rules consulted by the library routines. The way this happens is dictated by the `TZ` environment variable. As a side effect it also populates these variables: `tzname` (drawn from the `TZ` environment variable), `timezone` (seconds West of UTC outside DST), `altzone` (DST seconds west of UTC), and `daylight` (set to 0 when the zone carries no daylight saving rules at all, or to a nonzero value when daylight saving time applies at some point — whether in the past, the present, or the future).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Note

Even though adjusting the `TZ` environment variable will frequently change what functions such as `localtime()` produce without any `tzset()` call, do not depend on that side effect.

No whitespace belongs inside the `TZ` environment variable.

Here is the conventional layout of the `TZ` environment variable (extra spacing inserted here purely for legibility):

```python
std offset [dst [offset [,start[/time], end[/time]]]]

```

The pieces break down as follows:

`std` and `dst`

A run of three or more alphanumeric characters that names the timezone abbreviations. Their values flow through into time.tzname

`offset`

Its shape is `± hh[:mm[:ss]]`. The number here is what gets added to local time so as to reach UTC. A leading ‘-’ marks a timezone east of the Prime Meridian; without it the zone lies to the west. When dst is not trailed by an offset, summer time is taken to run one hour in front of standard time.

[Subject index](INDEX.md) · [Continue](mm-n-d.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md) · [Owning module, declaration or section: time.time](functions.md) · [Preceding source contract and version conditions](functions.md)
