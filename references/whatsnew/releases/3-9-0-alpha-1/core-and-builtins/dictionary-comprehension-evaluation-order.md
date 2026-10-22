# Python 3.9.0 alpha 1 / core and builtins / flipped evaluation order key value pairs dict comprehensions just

[bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224): Flipped the evaluation order of key: value pairs in dict comprehensions, just as PEP 572 proposed. That is, given `{k: v for ...}`, `k` is evaluated ahead of `v`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
