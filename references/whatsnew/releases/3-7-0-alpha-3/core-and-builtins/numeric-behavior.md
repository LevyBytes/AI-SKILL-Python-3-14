# Python 3.7.0 alpha 3 / core and builtins / numeric behavior

[bpo-20047](https://bugs.python.org/issue?@action=redirect&bpo=20047): As the docs say, the bytearray methods partition() and rpartition() now take only bytes-like objects as the separator. Specifically, handing in an integer separator now raises TypeError rather than yielding a nonsense result.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
