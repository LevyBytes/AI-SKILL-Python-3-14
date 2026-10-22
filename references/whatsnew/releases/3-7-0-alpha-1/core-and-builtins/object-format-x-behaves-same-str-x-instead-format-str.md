# Python 3.7.0 alpha 1 / core and builtins / object format x behaves same str x instead format str

[bpo-28974](https://bugs.python.org/issue?@action=redirect&bpo=28974): `object.__format__(x, '')` now behaves the same as `str(x)` instead of `format(str(self), '')`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
