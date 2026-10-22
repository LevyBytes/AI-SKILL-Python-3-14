# Python 3.5.0 alpha 1 / library / queue

[bpo-22185](https://bugs.python.org/issue?@action=redirect&bpo=22185): An intermittent RuntimeError inside threading.Condition.wait(), arising because the waiters queue was altered without the lock held, has been fixed. Doug Zongker supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
