# Python 3.10.0 alpha 1 / library / correct default missing duplicate valueerror does not end up

[bpo-39728](https://bugs.python.org/issue?@action=redirect&bpo=39728): Correct the default `_missing_` so that a duplicate `ValueError` does not end up as the `__context__` of the original `ValueError`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
