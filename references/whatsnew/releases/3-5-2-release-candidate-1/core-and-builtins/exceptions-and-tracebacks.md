# Python 3.5.2 release candidate 1 / core and builtins / exceptions and tracebacks

[bpo-22836](https://bugs.python.org/issue?@action=redirect&bpo=22836): Make sure that the exception output from PyErr_Display() and PyErr_WriteUnraisable() stays coherent even if rendering them triggers additional errors. The change touches what sys.__excepthook__() shows and the output produced when __del__() throws.

[bpo-27066](https://bugs.python.org/issue?@action=redirect&bpo=27066): Resolved a SystemError arising when a custom opener (for open()) hands back a negative number yet sets no exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
