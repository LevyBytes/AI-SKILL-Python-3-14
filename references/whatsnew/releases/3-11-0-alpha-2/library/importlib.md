# Python 3.11.0 alpha 2 / library / importlib

[bpo-35673](https://bugs.python.org/issue?@action=redirect&bpo=35673): Make the `__loader__` attribute easier to introspect for namespace packages. [`importlib.machinery.NamespaceLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.NamespaceLoader) is now public and fulfills the [`importlib.abc.InspectLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader) interface. For backward compatibility, `_NamespaceLoader` remains.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
