# Python 3.8.0 alpha 1 / core and builtins / veryhigh

[bpo-24596](https://bugs.python.org/issue?@action=redirect&bpo=24596): Within [`PyRun_SimpleFileExFlags()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyRun_SimpleFileExFlags), decref the module object before [`PyErr_Print()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Print) is called. Patch by Zackery Spytz.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
