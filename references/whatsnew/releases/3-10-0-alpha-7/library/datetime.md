# Python 3.10.0 alpha 7 / library / datetime

[bpo-43295](https://bugs.python.org/issue?@action=redirect&bpo=43295): When `'z'` is matched against the `%z` format specifier, [`datetime.datetime.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strptime) now throws `ValueError` rather than `IndexError`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
