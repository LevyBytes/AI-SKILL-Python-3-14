# Python 3.9.0 alpha 6 / library / threads and concurrency

[bpo-40089](https://bugs.python.org/issue?@action=redirect&bpo=40089): threading._after_fork() is corrected: when fork happened outside a thread that threading.Thread had spawned, threading._after_fork() will now build a _MainThread for _main_thread rather than a _DummyThread.

[bpo-40234](https://bugs.python.org/issue?@action=redirect&bpo=40234): Once more let daemon threads be spawned within subinterpreters (reverting the change that had forbidden them).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
