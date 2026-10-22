# Python 3.7.0 alpha 4 / tools demos / files and paths

[bpo-24960](https://bugs.python.org/issue?@action=redirect&bpo=24960): Rather than poking around the filesystem, 2to3 and lib2to3 are now able to load pickled grammar files via pkgutil.get_data(). The upshot is that 2to3 and lib2to3 keep working even when launched out of a zipfile.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
