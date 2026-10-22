# Python 3.9.0 beta 1 / library / time

[bpo-40192](https://bugs.python.org/issue?@action=redirect&bpo=40192): Under AIX, [`thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) is at this point built on `thread_cputime()`, whose resolution reaches nanoseconds, in place of `clock_gettime(CLOCK_THREAD_CPUTIME_ID)`, whose resolution is only 10 milliseconds. Batuhan Taskaya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
