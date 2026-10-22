# Python 3.9.0 alpha 1 / core and builtins / statistics

[bpo-38379](https://bugs.python.org/issue?@action=redirect&bpo=38379): Whenever cyclic garbage collection (gc) executes finalizers that bring unreachable objects back to life, the active gc pass terminates and gathers no cyclic trash. Yet the figures from `collect()` and `get_stats()` asserted that every bit of cyclic trash located had been collected, including the resurrected objects. The statistics were corrected to report that nothing was collected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
