# Python 3.8.0 alpha 4 / library / sys

[bpo-28552](https://bugs.python.org/issue?@action=redirect&bpo=28552): Made `distutils.sysconfig` cope when [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) is `None` or empty by seeding `project_base` from [`os.getcwd()`](https://docs.python.org/3.14/library/os.html#os.getcwd). The distutils build command was likewise corrected to skip `sys.executable` whenever it is `None` or empty.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
