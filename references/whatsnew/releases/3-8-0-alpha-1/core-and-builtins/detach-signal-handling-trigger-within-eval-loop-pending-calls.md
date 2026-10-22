# Python 3.8.0 alpha 1 / core and builtins / detach signal handling trigger within eval loop pending calls

[bpo-35423](https://bugs.python.org/issue?@action=redirect&bpo=35423): Detach the signal handling trigger within the eval loop from the "pending calls" machinery. No semantic change results and the performance difference is negligible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
