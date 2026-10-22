# Python 3.9.0 alpha 4 / library / collections

[bpo-39674](https://bugs.python.org/issue?@action=redirect&bpo=39674): Roll back the "Do not expose abstract collection classes in the collections module" change ([bpo-25988](https://bugs.python.org/issue?@action=redirect&bpo=25988)). ABC aliases such as collections.Mapping remain in Python 3.9 to smooth the migration away from Python 2.7, though they will be dropped in Python 3.10.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
