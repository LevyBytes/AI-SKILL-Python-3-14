# Python 3.6.3 release candidate 1 / library / signal setitimer can switch timer off handed very small value

[bpo-30807](https://bugs.python.org/issue?@action=redirect&bpo=30807): signal.setitimer() can switch the timer off when handed a very small value. Such tiny values (1e-6 for instance) count as legitimate non-zero arguments for setitimer(), whose interval resolution is documented as microseconds. On certain platforms, though, the routine that converts the value would turn 1e-6 into a zero-length interval, which switches the timer off rather than restarting it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
