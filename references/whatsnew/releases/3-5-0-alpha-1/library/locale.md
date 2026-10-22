# Python 3.5.0 alpha 1 / library / locale

[bpo-20076](https://bugs.python.org/issue?@action=redirect&bpo=20076): Non derived UTF-8 aliases were added to the locale aliases table.

[bpo-20079](https://bugs.python.org/issue?@action=redirect&bpo=20079): The locales that glibc 2.18 supports were added to the locale alias table.

[bpo-22410](https://bugs.python.org/issue?@action=redirect&bpo=22410): The re module's module level functions now cache compiled locale-dependent regular expressions while accounting for the locale.

[bpo-13918](https://bugs.python.org/issue?@action=redirect&bpo=13918): A locale.delocalize() function is now available; it strips locale-specific number formatting from a string that stands for a number, yet stops short of converting it to any particular type. Cédric Krier supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
