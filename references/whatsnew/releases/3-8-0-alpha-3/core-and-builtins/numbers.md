# Python 3.8.0 alpha 3 / core and builtins / numbers

[bpo-36048](https://bugs.python.org/issue?@action=redirect&bpo=36048): For implicitly converting Python numbers into C integers, the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) special method now takes over from [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__). Relying on the `__int__()` method during implicit conversions is now deprecated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
