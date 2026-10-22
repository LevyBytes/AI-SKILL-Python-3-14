# Python 3.9.0 alpha 1 / core and builtins / imports and modules

[bpo-38116](https://bugs.python.org/issue?@action=redirect&bpo=38116): The select module now meets PEP-384 and carries no static state any longer

[bpo-38076](https://bugs.python.org/issue?@action=redirect&bpo=38076): The struct module now achieves PEP-384 compatibility

[bpo-20490](https://bugs.python.org/issue?@action=redirect&bpo=20490): Anthony Sottile improved the import error message shown for a partially initialized module during circular `from` imports.

[bpo-37409](https://bugs.python.org/issue?@action=redirect&bpo=37409): Ben Lewis contributed a change ensuring that explicit relative imports issued from interactive sessions and scripts ? those lacking a parent package ? always raise ImportError instead of treating the active module as that package.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
