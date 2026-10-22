# Python 3.9.0 alpha 1 / library / inspect

[bpo-38026](https://bugs.python.org/issue?@action=redirect&bpo=38026): Repaired [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static), which relied on `isinstance` even though it ought to steer clear of dynamic lookup.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
