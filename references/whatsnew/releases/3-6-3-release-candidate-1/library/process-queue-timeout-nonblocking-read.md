# Python 3.6.3 release candidate 1 / library / timeout supplied multiprocessing queue get reads reader non blocking fashion if lock

[bpo-30595](https://bugs.python.org/issue?@action=redirect&bpo=30595): When a timeout is supplied, multiprocessing.Queue.get() now reads its reader in non-blocking fashion if the lock was obtained yet acquiring it ran past the supplied timeout.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
