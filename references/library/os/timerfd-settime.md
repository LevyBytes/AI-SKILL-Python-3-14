# os.timerfd_settime

os.timerfd_settime(*fd*, */*, ***, *flags=0*, *initial=0.0*, *interval=0.0*)

Adjust a timer file descriptor's internal timer. This function drives the same interval timer as `timerfd_settime_ns()`.

*fd* has to be a valid timer file descriptor.

You can adjust the timer's behaviour by supplying a *flags* value. Any of the variables below may be used, joined together with bitwise OR (the `|` operator):

- `TFD_TIMER_ABSTIME`

- `TFD_TIMER_CANCEL_ON_SET`

The timer gets disabled by setting *initial* to zero (`0`). When *initial* is greater than zero, the timer is enabled. When *initial* is less than zero, it raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception with `errno` set to [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL)

By default the timer fires once *initial* seconds have gone by.

However, when the `TFD_TIMER_ABSTIME` flag is set, the timer fires once the timer's clock (set by *clockid* in `timerfd_create()`) reaches *initial* seconds.

The timer's interval gets set by the *interval* [`float`](https://docs.python.org/3.14/library/functions.html#float). When *interval* is zero, the timer fires only once, at the initial expiration. When *interval* is greater than zero, the timer fires each time *interval* seconds have gone by since the previous expiration. When *interval* is less than zero, it raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) with `errno` set to [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL)

When the `TFD_TIMER_CANCEL_ON_SET` flag is set alongside `TFD_TIMER_ABSTIME` and this timer's clock is [`time.CLOCK_REALTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_REALTIME), the timer gets marked cancelable should the real-time clock change discontinuously. Reading the descriptor is aborted with the error ECANCELED.

Linux keeps the system clock as UTC. A daylight-savings time transition happens by changing the time offset only and does not bring about a discontinuous system clock change.

A discontinuous system clock change will be brought about by the following events:

- `settimeofday`

- `clock_settime`

- set the system date and time by `date` command

Give back a two-item tuple of (`next_expiration`, `interval`) drawn from the previous timer state, before this function ran.

See also

*[timerfd_create(2)](https://manpages.debian.org/timerfd_create(2))*, *[timerfd_settime(2)](https://manpages.debian.org/timerfd_settime(2))*, *[settimeofday(2)](https://manpages.debian.org/settimeofday(2))*, *[clock_settime(2)](https://manpages.debian.org/clock_settime(2))*, and *[date(1)](https://manpages.debian.org/date(1))*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

[Subject index](INDEX.md) · [Create a timer](timerfd-create.md) · [State and nanoseconds](timerfd-state-and-nanoseconds.md)
