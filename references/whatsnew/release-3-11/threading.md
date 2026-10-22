# What's New In Python 3.11 / threading — threading, time

### threading

- On Unix, whenever the `sem_clockwait()` function exists within the C library (glibc 2.30 and newer), the timeout in [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire) now relies on the monotonic clock ([`time.CLOCK_MONOTONIC`](https://docs.python.org/3.14/library/time.html#time.CLOCK_MONOTONIC)) in place of the system clock ([`time.CLOCK_REALTIME`](https://docs.python.org/3.14/library/time.html#time.CLOCK_REALTIME)), so that shifts in the system clock leave it unaffected. (Contributed by Victor Stinner in [bpo-41710](https://bugs.python.org/issue?@action=redirect&bpo=41710).)

[Subject index](INDEX.md) · [Previous source section](tempfile.md) · [Next source section](time.md) · [Release/subject declaration](summary-release-highlights.md)
