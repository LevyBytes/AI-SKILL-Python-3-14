# Python 3.6.4 release candidate 1 / library / build and platforms

[bpo-25532](https://bugs.python.org/issue?@action=redirect&bpo=25532): inspect.unwrap() now caps its unwrapping of an object at sys.getrecursionlimit() iterations, guarding against objects that build a fresh object during each attribute access.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
