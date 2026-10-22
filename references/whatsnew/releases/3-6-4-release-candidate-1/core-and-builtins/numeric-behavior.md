# Python 3.6.4 release candidate 1 / core and builtins / numeric behavior

[bpo-31293](https://bugs.python.org/issue?@action=redirect&bpo=31293): Repair crashes during true division and multiplication of a timedelta object by a float whose as_integer_ratio() method is bad. Oren Milman wrote the patch.

[bpo-20047](https://bugs.python.org/issue?@action=redirect&bpo=20047): The bytearray methods partition() and rpartition() now take only bytes-like objects for the separator, as the docs state. Specifically, passing an integer as a separator now raises TypeError instead of yielding a nonsensical result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
