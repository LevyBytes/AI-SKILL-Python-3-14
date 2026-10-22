# Python 3.9.0 alpha 5 / library / inspect

[bpo-13487](https://bugs.python.org/issue?@action=redirect&bpo=13487): Sidestep a potential *"RuntimeError: dictionary changed size during iteration"* arising from [`inspect.getmodule()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmodule) as it attempted to iterate over [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
