# Python 3.9.0 alpha 4 / library / numeric behavior

[bpo-39595](https://bugs.python.org/issue?@action=redirect&bpo=39595): Boosted performance of zipfile.Path on files holding a large number of entries. Performance was likewise improved and a minor issue resolved, as released with [importlib_metadata 1.5](https://importlib-metadata.readthedocs.io/en/latest/history.html#v1-5-0).

[bpo-39274](https://bugs.python.org/issue?@action=redirect&bpo=39274): `bool(fraction.Fraction)` now hands back a boolean even when (numerator != 0) fails to return a boolean (for instance: numpy number).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
