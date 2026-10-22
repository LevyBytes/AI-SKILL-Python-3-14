# Python 3.5.0 alpha 3 / library / signal

[bpo-23715](https://bugs.python.org/issue?@action=redirect&bpo=23715): [`signal.sigwaitinfo()`](https://docs.python.org/3.14/library/signal.html#signal.sigwaitinfo) together with [`signal.sigtimedwait()`](https://docs.python.org/3.14/library/signal.html#signal.sigtimedwait) now retry after a signal outside the *sigset* parameter interrupts them, provided the signal handler raises no exception. On retry, signal.sigtimedwait() recomputes the timeout against a monotonic clock.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
