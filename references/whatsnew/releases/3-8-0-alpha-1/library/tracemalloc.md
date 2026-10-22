# Python 3.8.0 alpha 1 / library / tracemalloc

[bpo-34228](https://bugs.python.org/issue?@action=redirect&bpo=34228): tracemalloc: the PYTHONTRACEMALLOC=0 environment variable along with the -X tracemalloc=0 command line option may now be supplied to switch tracemalloc off explicitly during startup.

[bpo-29564](https://bugs.python.org/issue?@action=redirect&bpo=29564): The warnings module now recommends turning on tracemalloc whenever the source is given, the tracemalloc module exists, yet tracemalloc is not currently tracking memory allocations.

[bpo-35053](https://bugs.python.org/issue?@action=redirect&bpo=35053): tracemalloc now attempts to refresh the traceback whenever an object is reused out of a "free list" (a speed-up for quicker object creation, employed by the builtin list type as one example).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
