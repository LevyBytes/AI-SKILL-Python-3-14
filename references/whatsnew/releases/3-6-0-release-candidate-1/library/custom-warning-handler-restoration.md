# Python 3.6.0 release candidate 1 / library / custom warning handler restoration

[bpo-28835](https://bugs.python.org/issue?@action=redirect&bpo=28835): Repair a regression in warnings.catch_warnings(): invoke warnings.showwarning() whenever it was replaced inside the context manager.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
