# Python 3.10.0 beta 1 / core and builtins / hash nan value tied object identity

[bpo-43475](https://bugs.python.org/issue?@action=redirect&bpo=43475): The hash of a NaN value is now tied to object identity. Previously every NaN hashed to 0 despite the fact that NaN values never compare equal. Sharing one hash across values that are not equal led to clustering inside hash tables.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
