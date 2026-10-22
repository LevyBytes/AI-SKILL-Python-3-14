# Python 3.11.0 alpha 1 / windows / threading

[bpo-41299](https://bugs.python.org/issue?@action=redirect&bpo=41299): Eliminate a 16 milliseconds jitter affecting timeouts in [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading), for instance through [`threading.Lock.acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire) or [`threading.Condition.wait()`](https://docs.python.org/3.14/library/threading.html#threading.Condition.wait).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
