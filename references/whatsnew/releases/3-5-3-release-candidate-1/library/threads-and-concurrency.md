# Python 3.5.3 release candidate 1 / library / threads and concurrency

[bpo-28427](https://bugs.python.org/issue?@action=redirect&bpo=28427): Stale keys should not strip new values out of a WeakValueDictionary while collection runs in a separate thread.

[bpo-19542](https://bugs.python.org/issue?@action=redirect&bpo=19542): Repair defects in WeakValueDictionary.setdefault() and WeakValueDictionary.pop() arising when a GC collection fires within another thread.

[bpo-28387](https://bugs.python.org/issue?@action=redirect&bpo=28387): Repair a possible crash in the _io.TextIOWrapper deallocator when the garbage collector fires within another thread. The work builds on a patch from Sebastian Cufre.

[bpo-27533](https://bugs.python.org/issue?@action=redirect&bpo=27533): Release the GIL within nt._isdir

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
