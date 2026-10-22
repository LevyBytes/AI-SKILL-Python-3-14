# Python 3.14.0 beta 3 / library / hashlib

[gh-134696](https://github.com/python/cpython/issues/134696): The built-in HACL* and OpenSSL implementations of hash function constructors now properly accept identical *documented* named arguments. As an example, [`md5()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.md5) could formerly be called as `md5(data=data)` or `md5(string=string)` depending on which implementation backed it, yet those two calls were not interchangeable. Bénédikt Tran authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
