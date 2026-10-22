# Python 3.5.4 release candidate 1 / core and builtins / steer clear blocking inside pthread mutex lock whenever pythread acquire lock told not

[bpo-30765](https://bugs.python.org/issue?@action=redirect&bpo=30765): Steer clear of blocking inside pthread_mutex_lock() whenever PyThread_acquire_lock() has been told not to block.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
