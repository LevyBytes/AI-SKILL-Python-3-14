# Python 3.8.0 alpha 1 / library / stop timeouts drifting whenever system clock changed executor map as completed

[bpo-34819](https://bugs.python.org/issue?@action=redirect&bpo=34819): To stop timeouts from drifting whenever the system clock is changed, `Executor.map()` and `as_completed()` now measure timeouts with a monotonic clock.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
