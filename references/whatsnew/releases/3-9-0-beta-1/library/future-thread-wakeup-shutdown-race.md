# Python 3.9.0 beta 1 / library / data race inside concurrent futures threadwakeup repaired shutdown lock guards every

[bpo-39995](https://bugs.python.org/issue?@action=redirect&bpo=39995): A data race inside concurrent.futures._ThreadWakeup was repaired: the shutdown lock now guards every access to _ThreadWakeup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
