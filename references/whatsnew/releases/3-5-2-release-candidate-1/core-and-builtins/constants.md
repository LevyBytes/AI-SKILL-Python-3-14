# Python 3.5.2 release candidate 1 / core and builtins / constants

[bpo-25843](https://bugs.python.org/issue?@action=redirect&bpo=25843): During compilation, constants are no longer combined when they compare equal yet differ in type. As an illustration, `f1, f2 = lambda: 1, lambda: 1.0` now compiles correctly into two separate functions: `f1()` returns `1` (`int`) while `f2()` returns `1.0` (`int`), even though `1` and `1.0` test as equal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
