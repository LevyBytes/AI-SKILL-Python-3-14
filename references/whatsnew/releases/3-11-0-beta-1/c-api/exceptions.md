# Python 3.11.0 beta 1 / c api / exceptions

[bpo-46343](https://bugs.python.org/issue?@action=redirect&bpo=46343): Two new functions, [`PyErr_GetHandledException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetHandledException) and [`PyErr_SetHandledException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetHandledException), arrive as easier stand-ins for [`PyErr_GetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetExcInfo) and [`PyErr_SetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetExcInfo).

The stable ABI carries both of them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
