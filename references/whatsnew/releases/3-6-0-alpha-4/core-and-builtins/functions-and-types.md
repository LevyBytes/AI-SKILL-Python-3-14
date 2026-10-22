# Python 3.6.0 alpha 4 / core and builtins / functions and types

[bpo-27366](https://bugs.python.org/issue?@action=redirect&bpo=27366): Implemented [**PEP 487**](https://peps.python.org/pep-0487/) (Simpler customization of class creation). When a class is subclassed, the base class has its __init_subclass__ classmethod invoked. After class creation, descriptors get initialized through __set_name__.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
