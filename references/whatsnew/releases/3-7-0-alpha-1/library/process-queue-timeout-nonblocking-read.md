# Python 3.7.0 alpha 1 / library / given timeout multiprocessing queue get reads reader non blocking mode whenever lock

[bpo-30595](https://bugs.python.org/issue?@action=redirect&bpo=30595): When given a timeout, multiprocessing.Queue.get() now reads from its reader in non-blocking mode whenever the lock was obtained but obtaining it overran the timeout.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
