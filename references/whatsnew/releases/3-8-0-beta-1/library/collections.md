# Python 3.8.0 beta 1 / library / collections

[bpo-36952](https://bugs.python.org/issue?@action=redirect&bpo=36952): As of Python 3.3, pulling ABCs out of [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) is deprecated; the import belongs to [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) instead. The ability to import from `collections` was earmarked for removal in 3.8, but that slipped to 3.9; the documentation and the `DeprecationWarning` were clarified.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
