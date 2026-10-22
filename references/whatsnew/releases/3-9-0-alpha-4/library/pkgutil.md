# Python 3.9.0 alpha 4 / library / pkgutil

[bpo-12915](https://bugs.python.org/issue?@action=redirect&bpo=12915): A fresh function `resolve_name` now lives in the `pkgutil` module. It turns a string shaped like `'a.b.c.d'` or `'a.b:c.d'` into an object. For that example, `a.b` names a package/module and `c.d` is an object inside that package/module reached through recursive attribute access.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
