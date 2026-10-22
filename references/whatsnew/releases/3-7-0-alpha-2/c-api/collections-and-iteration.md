# Python 3.7.0 alpha 2 / c api / collections and iteration

[bpo-28280](https://bugs.python.org/issue?@action=redirect&bpo=28280): `PyMapping_Keys()`, `PyMapping_Values()` and `PyMapping_Items()` now consistently hand back a `list` rather than possibly a `list` or a `tuple`. Oren Milman provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
