# Python 3.8.0 alpha 2 / core and builtins / monotonic condition wait clock

[bpo-12822](https://bugs.python.org/issue?@action=redirect&bpo=12822): Rely on the monotonic clock for `pthread_cond_timedwait` whenever `pthread_condattr_setclock` plus `CLOCK_MONOTONIC` exist.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
