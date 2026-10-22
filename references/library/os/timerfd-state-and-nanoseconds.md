# Timer descriptor state and nanosecond operations

os.timerfd_settime_ns(*fd*, */*, ***, *flags=0*, *initial=0*, *interval=0*)

Resembles `timerfd_settime()`, but treats time as nanoseconds. This function drives the same interval timer as `timerfd_settime()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

 os.timerfd_gettime(*fd*, */*)

Give back a two-item tuple of floats (`next_expiration`, `interval`).

`next_expiration` stands for the relative time before the timer fires again, no matter whether the `TFD_TIMER_ABSTIME` flag is set.

`interval` stands for the timer's interval. When zero, the timer fires only once, once `next_expiration` seconds have gone by.

See also

*[timerfd_gettime(2)](https://manpages.debian.org/timerfd_gettime(2))*

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

 os.timerfd_gettime_ns(*fd*, */*)

Resembles `timerfd_gettime()`, but gives back time as nanoseconds.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

 os.TFD_NONBLOCK

A flag for the `timerfd_create()` function, which sets the `O_NONBLOCK` status flag on the new timer file descriptor. When `TFD_NONBLOCK` is not set as a flag, `read()` blocks.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

[Subject index](INDEX.md) · [Create a timer](timerfd-create.md) · [Set a timer](timerfd-settime.md)
