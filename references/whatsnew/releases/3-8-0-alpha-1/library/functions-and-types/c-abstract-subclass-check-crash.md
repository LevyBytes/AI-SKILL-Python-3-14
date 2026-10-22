# Python 3.8.0 alpha 1 / library / repair c implementation abc subclasscheck cls subclass crashed whenever subclass

[bpo-32999](https://bugs.python.org/issue?@action=redirect&bpo=32999): Repair the C implementation of `ABC.__subclasscheck__(cls, subclass)` that crashed whenever `subclass` was not a type object.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
