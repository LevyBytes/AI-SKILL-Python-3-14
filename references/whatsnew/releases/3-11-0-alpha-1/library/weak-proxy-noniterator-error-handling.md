# Python 3.11.0 alpha 1 / library / weakref proxy objects point non iterators raise typeerror instead dereferencing null

[bpo-44720](https://bugs.python.org/issue?@action=redirect&bpo=44720): `weakref.proxy` objects that point at non-iterators now raise `TypeError` instead of dereferencing the null `tp_iternext` slot and bringing the interpreter down.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
