# Python 3.6.1 release candidate 1 / library / threads and concurrency

[bpo-29376](https://bugs.python.org/issue?@action=redirect&bpo=29376): Repair the assertion error within threading._DummyThread.is_alive().

[bpo-28969](https://bugs.python.org/issue?@action=redirect&bpo=28969): Corrected a race condition within the C implementation of functools.lru_cache. KeyError could surface whenever a cached function holding a full cache was called at the same time from separate threads using identical uncached arguments.

[bpo-28427](https://bugs.python.org/issue?@action=redirect&bpo=28427): Old keys ought not to wipe out new values from a WeakValueDictionary while collecting from a different thread.

[bpo-19542](https://bugs.python.org/issue?@action=redirect&bpo=19542): Repair bugs within WeakValueDictionary.setdefault() and WeakValueDictionary.pop() whenever a GC collection takes place on a different thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
