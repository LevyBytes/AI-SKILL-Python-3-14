# Python 3.7.0 beta 5 / library / leave arguments typing union unsimplified

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Leave the arguments to `typing.Union` unsimplified. From now on `Union[Manager, Employee]` won't collapse to `Employee` at runtime. That collapsing had previously triggered multiple bugs and narrowed what introspection could do.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
