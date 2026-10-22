# Python 3.10.0 alpha 3 / security / marked accumulator variable inside hmac compare digest volatile makes optimizations defeat

[bpo-40791](https://bugs.python.org/issue?@action=redirect&bpo=40791): Marked the accumulator variable inside `hmac.compare_digest` as `volatile`, which makes optimizations that defeat constant-time behavior less probable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
