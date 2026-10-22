# Python 3.11.0 alpha 2 / core and builtins / repaired crash within issubclass triggered unbounded recursion while traversing

[bpo-30570](https://bugs.python.org/issue?@action=redirect&bpo=30570): Repaired a crash within `issubclass()` triggered by unbounded recursion while traversing pathological `__bases__` tuples.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
