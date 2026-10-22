# Python 3.5.0 release candidate 2 / core and builtins / imports and modules

[bpo-24492](https://bugs.python.org/issue?@action=redirect&bpo=24492): If a "package" has no __name__ attribute while a `from .. import ...` statement is attempted, an ImportError is now raised in place of an AttributeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
