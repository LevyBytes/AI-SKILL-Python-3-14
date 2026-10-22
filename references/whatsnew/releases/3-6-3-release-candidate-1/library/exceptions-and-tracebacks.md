# Python 3.6.3 release candidate 1 / library / exceptions and tracebacks

[bpo-31234](https://bugs.python.org/issue?@action=redirect&bpo=31234): socket.create_connection() now manually fixes a reference cycle by clearing, on success, the variable that holds the last exception.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
