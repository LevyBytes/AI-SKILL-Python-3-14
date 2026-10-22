# Python 3.10.0 alpha 6 / core and builtins / constants

[bpo-38302](https://bugs.python.org/issue?@action=redirect&bpo=38302): Should [`object.__ipow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__ipow__) return [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented), the operator now correctly falls back, as one would expect, to [`object.__pow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__pow__) and [`object.__rpow__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rpow__).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
