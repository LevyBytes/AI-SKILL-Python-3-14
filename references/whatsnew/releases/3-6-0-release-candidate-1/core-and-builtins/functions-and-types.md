# Python 3.6.0 release candidate 1 / core and builtins / functions and types

[bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722): Where previously a class was quietly produced that couldn't support zero-argument `super()` inside methods, omitting to forward the new `__classcell__` namespace entry to `type.__new__` now triggers a `DeprecationWarning` while still yielding a class that supports zero-argument `super()`.

[bpo-28797](https://bugs.python.org/issue?@action=redirect&bpo=28797): Altering the class __dict__ from within a descriptor's __set_name__ method, where that descriptor lives in the same class, no longer blocks the __set_name__ method of the other descriptors from running.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
