# Python 3.7.0 alpha 4 / core and builtins / platform

[bpo-32260](https://bugs.python.org/issue?@action=redirect&bpo=32260): On big-endian platforms, refrain from byte swapping the input keys for the SipHash algorithm. Doing so should make siphash return consistent results from one platform to another.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
