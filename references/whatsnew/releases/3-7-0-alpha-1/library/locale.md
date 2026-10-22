# Python 3.7.0 alpha 1 / library / locale

[bpo-30215](https://bugs.python.org/issue?@action=redirect&bpo=30215): Compiled regular expression objects carrying the re.LOCALE flag no longer hinge on the locale present at compile time. The outcome of matching is governed solely by the locale active while matching.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
