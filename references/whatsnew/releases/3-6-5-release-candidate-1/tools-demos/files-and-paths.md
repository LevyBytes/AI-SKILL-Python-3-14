# Python 3.6.5 release candidate 1 / tools demos / files and paths

[bpo-24960](https://bugs.python.org/issue?@action=redirect&bpo=24960): Both 2to3 and lib2to3 can now load pickled grammar files through pkgutil.get_data() instead of poking at the filesystem. As a result 2to3 and lib2to3 will operate when launched from a zipfile.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
