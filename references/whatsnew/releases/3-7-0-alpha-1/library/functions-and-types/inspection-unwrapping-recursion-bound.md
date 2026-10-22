# Python 3.7.0 alpha 1 / library / inspect unwrap will attempt unwrap object most sys getrecursionlimit times guarding

[bpo-25532](https://bugs.python.org/issue?@action=redirect&bpo=25532): inspect.unwrap() will from now on attempt to unwrap an object at most sys.getrecursionlimit() times, guarding against objects that manufacture a fresh object on every attribute access.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
