# Python 3.11.0 alpha 4 / c api / import

[bpo-45855](https://bugs.python.org/issue?@action=redirect&bpo=45855): Across stdlib modules, the deprecated use of [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock) was swapped out for [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule). Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
