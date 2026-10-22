# time: Boot, monotonic, process and thread clock identifiers

### Clock ID Constants

You pass these constants as arguments to `clock_getres()` and `clock_gettime()`.

 time.CLOCK_BOOTTIME

The same as `CLOCK_MONOTONIC`, with the added wrinkle that it folds in whatever time the system spends suspended.

That lets programs obtain a suspend-aware monotonic clock and skip the headaches of `CLOCK_REALTIME`, whose readings can jump whenever the time is reset via `settimeofday()` or something comparable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.39.

Added in version 3.7.

 time.CLOCK_HIGHRES

Solaris OS ships a `CLOCK_HIGHRES` timer that strives to draw on the best available hardware source and can approach nanosecond resolution. `CLOCK_HIGHRES` serves as the high-resolution clock that cannot be adjusted.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Solaris.

Added in version 3.3.

 time.CLOCK_MONOTONIC

A clock that is unsettable and stands for monotonic time counted from an unstated origin.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 time.CLOCK_MONOTONIC_RAW

Comparable to `CLOCK_MONOTONIC`, yet it exposes a raw hardware-derived time that NTP adjustments leave untouched.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.28, macOS >= 10.12.

Added in version 3.3.

 time.CLOCK_MONOTONIC_RAW_APPROX

Resembles `CLOCK_MONOTONIC_RAW`, except it pulls a value the system caches at each context switch, trading away some accuracy.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): macOS >= 10.12.

Added in version 3.13.

 time.CLOCK_PROCESS_CPUTIME_ID

A fine-grained per-process timer sourced from the CPU.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 time.CLOCK_PROF

A high-resolution timer scoped to one process and provided by the CPU.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): FreeBSD, NetBSD >= 7, OpenBSD.

Added in version 3.7.

 time.CLOCK_TAI

[International Atomic Time](https://www.nist.gov/pml/time-and-frequency-division/how-utcnist-related-coordinated-universal-time-utc-international)

For this to return the right answer, the system needs an up-to-date leap second table. Such a table can be kept current by PTP or NTP software.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux.

Added in version 3.9.

 time.CLOCK_THREAD_CPUTIME_ID

A CPU-time clock tied to an individual thread.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](mm-n-d.md) · [Continue](time-clock-uptime-to-time-clock-realtime.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md)
