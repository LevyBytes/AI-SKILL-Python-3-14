# Python 3.7.0 alpha 4 / core and builtins / constants

[bpo-30416](https://bugs.python.org/issue?@action=redirect&bpo=30416): During constant folding the optimizer is now guarded against burning lots of time on heavy calculations and eating lots of memory while building large constants. The limits on constants producible through constant folding were raised.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
