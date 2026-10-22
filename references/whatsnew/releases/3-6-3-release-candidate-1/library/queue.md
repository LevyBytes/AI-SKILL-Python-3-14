# Python 3.6.3 release candidate 1 / library / queue

[bpo-30886](https://bugs.python.org/issue?@action=redirect&bpo=30886): Repaired multiprocessing.Queue.join_thread(): the call now blocks until that thread finishes, including when the very process that built the queue is the one that launched the thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
