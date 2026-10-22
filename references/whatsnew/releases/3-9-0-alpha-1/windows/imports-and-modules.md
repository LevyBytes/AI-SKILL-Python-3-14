# Python 3.9.0 alpha 1 / windows / imports and modules

[bpo-36266](https://bugs.python.org/issue?@action=redirect&bpo=36266): When a DLL fails to load while a module is imported inside `_PyImport_FindSharedFuncptrWindows()`, the module's name is now included in the formatted error text. Srinivas Nyayapati supplied the patch.

[bpo-37778](https://bugs.python.org/issue?@action=redirect&bpo=37778): Fixes the icons used for file associations to the Microsoft Store package.

[bpo-37672](https://bugs.python.org/issue?@action=redirect&bpo=37672): Make the Windows Store package's pip rely on the bundled `pip.ini` in place of the `PIP_USER` variable.

[bpo-38519](https://bugs.python.org/issue?@action=redirect&bpo=38519): Brings back the internal C headers that the nuget.org and Microsoft Store packages had been lacking.

[bpo-38114](https://bugs.python.org/issue?@action=redirect&bpo=38114): The `pip.ini` is no longer included in the Nuget package.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
