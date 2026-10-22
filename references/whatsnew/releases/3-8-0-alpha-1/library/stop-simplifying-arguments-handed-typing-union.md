# Python 3.8.0 alpha 1 / library / stop simplifying arguments handed typing union

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Stop simplifying arguments handed to `typing.Union`. As of now `Union[Manager, Employee]` is not reduced to `Employee` at runtime. That kind of simplification formerly led to several bugs and constrained the options for introspection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
