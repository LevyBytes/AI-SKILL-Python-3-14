# Python 3.8.0 alpha 1 / c api / functions and types

[bpo-34193](https://bugs.python.org/issue?@action=redirect&bpo=34193): Correct the pluralization within TypeError messages from getargs.c plus typeobject.c: "1 argument" rather than "1 arguments", and "1 element" rather than "1 elements".

[bpo-33042](https://bugs.python.org/issue?@action=redirect&bpo=33042): Apps that embed Python may again invoke PySys_ResetWarnOptions, PySys_AddWarnOption, and PySys_AddXOption before they call Py_Initialize.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
