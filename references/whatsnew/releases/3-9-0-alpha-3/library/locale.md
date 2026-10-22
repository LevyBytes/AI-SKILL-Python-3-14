# Python 3.9.0 alpha 3 / library / locale

[bpo-38536](https://bugs.python.org/issue?@action=redirect&bpo=38536): A trailing space is no longer left in formatted currency when `international=True` and the locale places the symbol after the value. For example, `locale.currency(12.34, international=True)` used to yield `'12,34 EUR '` rather than `'12,34 EUR'`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
