# Python 3.6.0 beta 1 / core and builtins / threads and concurrency

[bpo-27558](https://bugs.python.org/issue?@action=redirect&bpo=27558): Corrects a SystemError in how the “raise” statement is implemented. Within a freshly created thread, a RuntimeError is raised because no active exception exists to reraise. Xiang Zhang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
