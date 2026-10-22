# Python 3.7.0 alpha 1 / build / imports and modules

[bpo-21124](https://bugs.python.org/issue?@action=redirect&bpo=21124): Repair the _struct module build on Cygwin by handing `NULL` rather than `&PyType_Type` to PyVarObject_HEAD_INIT. Masayuki Yamamoto supplied the patch.

[bpo-13756](https://bugs.python.org/issue?@action=redirect&bpo=13756): Repair extension module builds on Cygwin. Roumen Petrov contributed the patch, building on an original by Jason Tishler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
