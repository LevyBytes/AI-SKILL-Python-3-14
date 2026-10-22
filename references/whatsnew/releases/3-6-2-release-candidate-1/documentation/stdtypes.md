# Python 3.6.2 release candidate 1 / documentation / stdtypes

[bpo-30052](https://bugs.python.org/issue?@action=redirect&bpo=30052): The link targets of [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) now resolve to their respective type definitions instead of the matching builtin function entries. To reference the latter, use [bytes](https://docs.python.org/3.14/library/functions.html#func-bytes) and [bytearray](https://docs.python.org/3.14/library/functions.html#func-bytearray). So that this update and later cross-reference updates apply on their own, the daily documentation builds now switch off Sphinx's default output caching features.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
