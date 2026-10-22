# Python 3.7.0 alpha 1 / documentation / stdtypes

[bpo-30052](https://bugs.python.org/issue?@action=redirect&bpo=30052): the link targets for [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) now point at their respective type definitions instead of the matching builtin function entries. Reach for [bytes](https://docs.python.org/3.14/library/functions.html#func-bytes) and [bytearray](https://docs.python.org/3.14/library/functions.html#func-bytearray) when referencing the latter. So that this and later cross-reference updates apply on their own, the daily documentation builds now switch off Sphinx's default output caching features.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
