# Python 3.10.0 alpha 3 / build / imports and modules

[bpo-38823](https://bugs.python.org/issue?@action=redirect&bpo=38823): Building the `_ctypes` extension module without the `wchar_t` type is no longer possible: the `CTYPES_UNICODE` macro is removed. In any case the `wchar_t` type is needed to build Python at all. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
