# Python 3.13.0 alpha 4 / core and builtins / functions and types

[gh-113462](https://github.com/python/cpython/issues/113462): Cap how many versions any single class may consume. This stops a handful of misbehaving classes from exhausting the whole supply of version numbers.

[gh-114806](https://github.com/python/cpython/issues/114806): Stop specializing calls to classes whenever those classes carry metaclasses. This corrects a defect in which the metaclass `__call__` method went uncalled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
