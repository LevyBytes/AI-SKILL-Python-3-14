# Python 3.12.0 alpha 6 / core and builtins / repair systemerror segmentation fault iter reduce happened internal access

[gh-101765](https://github.com/python/cpython/issues/101765): Repair a SystemError / segmentation fault in iter `__reduce__` that happened when internal access of `builtins.__dict__` keys mutates the iter object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
