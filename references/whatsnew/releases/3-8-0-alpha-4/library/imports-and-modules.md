# Python 3.8.0 alpha 4 / library / imports and modules

[bpo-31904](https://bugs.python.org/issue?@action=redirect&bpo=31904): Bring in time module support and clear up the test_time failures under VxWorks.

[bpo-13611](https://bugs.python.org/issue?@action=redirect&bpo=13611): C14N 2.0 serialisation is now supported by the xml.etree.ElementTree packages. Stefan Behnel authored the patch.

[bpo-36575](https://bugs.python.org/issue?@action=redirect&bpo=36575): By default the `_lsprof` module now relies on the same internal timer as `time.perf_counter()`. Formerly `gettimeofday(2)` served on Unix. The replacement offers finer resolution across most Unix systems, and because `perf_counter()` is monotonic the measurements no longer shift when the system clock is adjusted. Inada Naoki supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
