# Python 3.9.0 alpha 4 / core and builtins / memory and lifetimes

[bpo-39382](https://bugs.python.org/issue?@action=redirect&bpo=39382): Resolve a use-after-free along the single-inheritance branch of `issubclass()`, triggered when an object's `__bases__` holds a single reference and its first item likewise does. Yonatan Goldschmidt supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
