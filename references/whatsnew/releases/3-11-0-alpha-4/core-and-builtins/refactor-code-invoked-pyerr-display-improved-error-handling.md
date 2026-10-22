# Python 3.11.0 alpha 4 / core and builtins / refactor code invoked pyerr display improved error handling

[bpo-45635](https://bugs.python.org/issue?@action=redirect&bpo=45635): A refactor of the code invoked from `_PyErr_Display()` improved its error handling. The routine now returns at once when an unrecoverable error occurs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
