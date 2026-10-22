# Python 3.5.1 release candidate 1 / core and builtins / threads and concurrency

[bpo-25274](https://bugs.python.org/issue?@action=redirect&bpo=25274): sys.setrecursionlimit() now raises a RecursionError whenever the requested limit is too low for the present recursion depth. The "lower-water mark" formula was also adjusted to stay monotonic. That mark governs when the thread state's overflowed flag is cleared.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
