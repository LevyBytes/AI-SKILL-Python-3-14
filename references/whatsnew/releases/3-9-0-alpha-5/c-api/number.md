# Python 3.9.0 alpha 5 / c api / number

[bpo-38643](https://bugs.python.org/issue?@action=redirect&bpo=38643): Rather than crashing when handed an invalid base, [`PyNumber_ToBase()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_ToBase) now raises a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
