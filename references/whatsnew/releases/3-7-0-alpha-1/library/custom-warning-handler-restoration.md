# Python 3.7.0 alpha 1 / library / custom warning handler restoration

[bpo-28835](https://bugs.python.org/issue?@action=redirect&bpo=28835): Corrected a regression that had crept into warnings.catch_warnings(): warnings.showwarning() is invoked when something overrode it inside the context manager.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
