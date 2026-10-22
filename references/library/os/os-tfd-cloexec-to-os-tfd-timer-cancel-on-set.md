# os — Timer File Descriptors

os.TFD_CLOEXEC

A flag for the `timerfd_create()` function. When `TFD_CLOEXEC` is set as a flag, the close-on-exec flag gets applied to the new file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

 os.TFD_TIMER_ABSTIME

A flag for the `timerfd_settime()` and `timerfd_settime_ns()` functions. With this flag set, *initial* is taken as an absolute point on the timer's clock (measured in UTC seconds or nanoseconds counted from the Unix Epoch).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

 os.TFD_TIMER_CANCEL_ON_SET

A flag for the `timerfd_settime()` and `timerfd_settime_ns()` functions alongside `TFD_TIMER_ABSTIME`. The timer gets cancelled once the time of the underlying clock changes discontinuously.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](timerfd-settime.md) · [Continue](os-getxattr-to-os-xattr-replace.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Timer File Descriptors](timerfd-create.md)
