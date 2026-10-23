# What's New In Python 3.9 / time - time

### time

On AIX, [`thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) is now backed by `thread_cputime()`, which offers nanosecond resolution, in place of `clock_gettime(CLOCK_THREAD_CPUTIME_ID)`, whose resolution is only 10 milliseconds. (Contributed by Batuhan Taskaya in [bpo-40192](https://bugs.python.org/issue?@action=redirect&bpo=40192))

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](sys.md) · [Release/subject declaration](summary-release-highlights.md)
