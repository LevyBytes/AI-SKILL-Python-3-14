# Python 3.9.0 alpha 1 / c api / arg

[bpo-38540](https://bugs.python.org/issue?@action=redirect&bpo=38540): Closed a possible leak inside [`PyArg_Parse()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_Parse) and kindred functions for the format units `"es#"` and `"et#"` whenever the macro `PY_SSIZE_T_CLEAN` goes undefined.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
