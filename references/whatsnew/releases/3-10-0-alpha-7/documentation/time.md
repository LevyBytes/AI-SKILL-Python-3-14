# Python 3.10.0 alpha 7 / documentation / time

[bpo-43407](https://bugs.python.org/issue?@action=redirect&bpo=43407): Made clear that a value returned by [`time.monotonic()`](https://docs.python.org/3.14/library/time.html#time.monotonic), [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter), [`time.process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time), or [`time.thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) is comparable against the value from any later call to that same function — not solely the very next call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
