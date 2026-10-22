# Python 3.9.0 alpha 6 / library / threading

[bpo-40089](https://bugs.python.org/issue?@action=redirect&bpo=40089): Introduce a private `_at_fork_reinit()` method on the `_thread.Lock`, `_thread.RLock`, [`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock), and [`threading.Condition`](https://docs.python.org/3.14/library/threading.html#threading.Condition) classes, which reinitializes the lock during fork inside the child process and returns it to the unlocked state. The private `_reset_internal_locks()` method on [`threading.Event`](https://docs.python.org/3.14/library/threading.html#threading.Event) is likewise renamed to `_at_fork_reinit()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
