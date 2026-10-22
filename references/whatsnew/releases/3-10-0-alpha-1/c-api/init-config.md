# Python 3.10.0 alpha 1 / c api / init config

[bpo-40910](https://bugs.python.org/issue?@action=redirect&bpo=40910): Explicitly publish the [`Py_GetArgcArgv()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_GetArgcArgv) function in the C API and document it. It used to be exported implicitly, something that stopped working once Python started being built with `-fvisibility=hidden`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
