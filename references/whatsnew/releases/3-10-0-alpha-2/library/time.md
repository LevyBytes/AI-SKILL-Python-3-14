# Python 3.10.0 alpha 2 / library / time

[bpo-35455](https://bugs.python.org/issue?@action=redirect&bpo=35455): Under Solaris, [`thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) is now built atop `gethrvtime()` since `clock_gettime(CLOCK_THREAD_CPUTIME_ID)` cannot always be relied upon. Jakub Kulik supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
