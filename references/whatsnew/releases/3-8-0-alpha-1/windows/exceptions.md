# Python 3.8.0 alpha 1 / windows / exceptions

[bpo-29097](https://bugs.python.org/issue?@action=redirect&bpo=29097): Repair a defect where `datetime.fromtimestamp()` wrongly raised an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) under Windows for values from 0 through 86400. Patch contributed by Ammar Askar.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
