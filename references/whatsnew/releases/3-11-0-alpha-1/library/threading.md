# Python 3.11.0 alpha 1 / library / threading

[bpo-44422](https://bugs.python.org/issue?@action=redirect&bpo=44422): A reentrant lock is now used by the [`threading.enumerate()`](https://docs.python.org/3.14/library/threading.html#threading.enumerate) function to avoid hanging on a reentrant call. Victor Stinner wrote the patch.

[bpo-41710](https://bugs.python.org/issue?@action=redirect&bpo=41710): On Unix, when the `sem_clockwait()` function exists in the C library (glibc 2.30 and later), the [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire) method now relies on the monotonic clock ([`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC)) for its timeout instead of the system clock ([`time.CLOCK_REALTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_REALTIME)), so it stays unaffected by system clock changes. Victor Stinner wrote the patch.

[bpo-1596321](https://bugs.python.org/issue?@action=redirect&bpo=1596321): Corrected the `threading._shutdown()` function for the case where the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module was first imported from a thread other than the main one: it no longer logs an error during Python exit.

[bpo-45274](https://bugs.python.org/issue?@action=redirect&bpo=45274): Corrected a race condition within the [`Thread.join()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join) method of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module. Should a signal interrupt the function and its handler raise an exception, the thread is kept in a consistent state so no deadlock occurs. Victor Stinner wrote the patch.

[bpo-24391](https://bugs.python.org/issue?@action=redirect&bpo=24391): Better reprs now appear for these [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) synchronization objects: [`Semaphore`](https://docs.python.org/3.14/library/threading.html#threading.Semaphore), [`BoundedSemaphore`](https://docs.python.org/3.14/library/threading.html#threading.BoundedSemaphore), [`Event`](https://docs.python.org/3.14/library/threading.html#threading.Event) and [`Barrier`](https://docs.python.org/3.14/library/threading.html#threading.Barrier).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
