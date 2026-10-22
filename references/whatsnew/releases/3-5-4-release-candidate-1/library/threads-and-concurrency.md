# Python 3.5.4 release candidate 1 / library / threads and concurrency

[bpo-30414](https://bugs.python.org/issue?@action=redirect&bpo=30414): The background thread running multiprocessing.Queue._feed no longer breaks out of its main loop on an exception.

[bpo-30886](https://bugs.python.org/issue?@action=redirect&bpo=30886): Repair multiprocessing.Queue.join_thread(): it now holds until the thread finishes, even when that thread was launched by the very process that created the queue.

[bpo-29376](https://bugs.python.org/issue?@action=redirect&bpo=29376): Resolve an assertion failure raised by threading._DummyThread.is_alive().

[bpo-28969](https://bugs.python.org/issue?@action=redirect&bpo=28969): Resolve a race condition inside the C implementation of functools.lru_cache. A KeyError might surface when a cached function whose cache was full got called at the same moment from separate threads using identical uncached arguments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
