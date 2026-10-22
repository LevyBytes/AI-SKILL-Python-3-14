# Python 3.5.2 release candidate 1 / core and builtins / crash object reduce fixed situation where slot name freed inside

[bpo-24097](https://bugs.python.org/issue?@action=redirect&bpo=24097): A crash in object.__reduce__() is fixed for the situation where a slot name is freed from inside __getattr__.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
