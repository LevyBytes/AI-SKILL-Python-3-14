# Python 3.5.0 alpha 1 / library / fstat failure signal set wakeup fd raises oserror place valueerror

[bpo-22018](https://bugs.python.org/issue?@action=redirect&bpo=22018): On a `fstat()` failure, signal.set_wakeup_fd() now raises an OSError in place of a ValueError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
