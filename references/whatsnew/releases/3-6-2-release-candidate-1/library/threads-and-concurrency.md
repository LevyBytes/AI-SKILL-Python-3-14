# Python 3.6.2 release candidate 1 / library / threads and concurrency

[bpo-30414](https://bugs.python.org/issue?@action=redirect&bpo=30414): The multiprocessing.Queue._feed thread running in the background no longer escapes its main loop upon an exception.

[bpo-30038](https://bugs.python.org/issue?@action=redirect&bpo=30038): Repaired a race condition spanning signal delivery and the wakeup file descriptor. Nathaniel Smith wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
