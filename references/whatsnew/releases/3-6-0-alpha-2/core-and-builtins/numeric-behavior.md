# Python 3.6.0 alpha 2 / core and builtins / numeric behavior

[bpo-26983](https://bugs.python.org/issue?@action=redirect&bpo=26983): float() now consistently hands back an instance of the exact float type. A deprecation warning fires whenever __float__ yields an instance of a strict subclass of float. A later Python version may turn this into an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
