# Python 3.14.5 release candidate 1 / build / imports and modules

[gh-146264](https://github.com/python/cpython/issues/146264): Repair static-module builds on targets other than WASI: with `MODULE_BUILDTYPE=static`, the HACL dependencies are now linked as static libraries, which keeps duplicate `_Py_LibHacl_*` symbol errors from appearing during linking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
