# Python 3.7.0 alpha 1 / library / close method zip entry writer object may invoked more

[bpo-30017](https://bugs.python.org/issue?@action=redirect&bpo=30017): The close() method on a zip entry writer object may now be invoked more than once. Any write to a closed writer now always raises a ValueError.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
