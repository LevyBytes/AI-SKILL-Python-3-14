# Python 3.5.3 release candidate 1 / core and builtins / threads and concurrency

[bpo-27558](https://bugs.python.org/issue?@action=redirect&bpo=27558): Repair a SystemError in how the "raise" statement is implemented. Inside a freshly created thread, raise a RuntimeError because no active exception exists to reraise. Xiang Zhang authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
