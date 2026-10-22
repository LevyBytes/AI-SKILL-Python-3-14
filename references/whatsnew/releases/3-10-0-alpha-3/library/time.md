# Python 3.10.0 alpha 3 / library / time

[bpo-37205](https://bugs.python.org/issue?@action=redirect&bpo=37205): The [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time), [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) and [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) functions no longer abort with a Python fatal error; instead they raise an ordinary Python exception when they fail.

[bpo-37205](https://bugs.python.org/issue?@action=redirect&bpo=37205): [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) under Windows and [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic) under macOS are now system-wide. Formerly each applied a startup-computed offset to lessen the precision loss the float type introduces. Reach for [`time.perf_counter_ns()`](https://docs.python.org/3.14/library/time.html#time.perf_counter_ns) and [`time.monotonic_ns()`](https://docs.python.org/3.14/library/time.html#time.monotonic_ns), introduced in Python 3.7, to sidestep that precision loss.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
