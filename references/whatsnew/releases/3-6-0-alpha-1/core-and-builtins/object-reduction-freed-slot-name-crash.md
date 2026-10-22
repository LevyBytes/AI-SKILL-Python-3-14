# Python 3.6.0 alpha 1 / core and builtins / repair crash object reduce struck slot name freed inside getattr

[bpo-24097](https://bugs.python.org/issue?@action=redirect&bpo=24097): Repair the crash in object.__reduce__() that struck when a slot name was freed inside __getattr__.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
