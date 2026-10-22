# Python 3.14.0 beta 4 / library / zoneinfo

[gh-85702](https://github.com/python/cpython/issues/85702): When `zoneinfo._common.load_tzdata` receives a package lacking a resource, a [`zoneinfo.ZoneInfoNotFoundError`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfoNotFoundError) now gets raised in place of a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). Victor Stinner authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
