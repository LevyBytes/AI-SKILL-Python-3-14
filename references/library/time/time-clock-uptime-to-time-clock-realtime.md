# time: `time.CLOCK_UPTIME`, `time.CLOCK_UPTIME_RAW`, `time.CLOCK_UPTIME_RAW_APPROX`, `time.CLOCK_REALTIME`

time.CLOCK_UPTIME

A time whose absolute reading equals how long the system has been up and not suspended, yielding precise uptime figures for both absolute readings and intervals.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD, OpenBSD >= 5.5.

Added in version 3.7.

 time.CLOCK_UPTIME_RAW

A clock that advances monotonically, counting from some arbitrary origin, immune to frequency or time adjustments and held still whenever the system sleeps.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): macOS >= 10.12.

Added in version 3.8.

 time.CLOCK_UPTIME_RAW_APPROX

Akin to `CLOCK_UPTIME_RAW`, but because the value gets cached by the system at context switches it carries less accuracy.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): macOS >= 10.12.

Added in version 3.13.

This next constant is the sole argument that may be handed to `clock_settime()`.

 time.CLOCK_REALTIME

The real-time clock. Adjusting it calls for suitable privileges. Every process shares one and the same clock.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](time-clock-boottime-to-time-clock-thread-cputime-id.md) · [Continue](time-altzone-to-time-tzname.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Clock ID Constants](time-clock-boottime-to-time-clock-thread-cputime-id.md)
