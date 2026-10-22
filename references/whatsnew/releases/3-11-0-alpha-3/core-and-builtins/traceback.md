# Python 3.11.0 alpha 3 / core and builtins / traceback

[bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711): The function `_PyErr_ChainStackItem()` will no longer normalize `exc_info` (a step that formerly included attaching the traceback to the exception instance), since `exc_info` is always normalized already.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
