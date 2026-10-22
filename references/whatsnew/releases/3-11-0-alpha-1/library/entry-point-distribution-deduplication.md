# Python 3.11.0 alpha 1 / library / inside importlib metadata entry points removing duplicate distributions no longer needs full

[bpo-44246](https://bugs.python.org/issue?@action=redirect&bpo=44246): Inside importlib.metadata.entry_points, removing duplicate distributions no longer needs the full metadata of PathDistribution objects to be loaded, which speeds entry point loading by roughly 10x.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
