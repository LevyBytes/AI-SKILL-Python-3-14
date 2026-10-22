# Python 3.11.0 alpha 3 / core and builtins / sys

[bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711): Each of the three `exc_info` values is now kept mutually consistent. Specifically, the exception instance is now the source from which the `type` and `traceback` fields are derived. That alters what [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) and [`PyErr_GetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetExcInfo) return whenever the exception instance gets modified during handling, and it likewise affects [`PyErr_SetExcInfo()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetExcInfo), which from now on disregards the `type` and `traceback` arguments passed to it.

[bpo-45582](https://bugs.python.org/issue?@action=redirect&bpo=45582): The path calculation (referred to as `getpath`) has been rebuilt as a frozen Python module. No visible difference is expected, though it could affect how every path surfaced through [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) and [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) gets computed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
