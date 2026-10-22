# Python 3.6.0 alpha 4 / core and builtins / imports and modules

[bpo-27419](https://bugs.python.org/issue?@action=redirect&bpo=27419): When importing submodules or doing a "from import", the standard __import__() no longer consults "__import__" in globals or builtins. A crash was fixed for the case of warning about being unable to resolve a package from __spec__ or __package__.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
