# Python 3.9.0 alpha 1 / windows / os path

[bpo-1311](https://bugs.python.org/issue?@action=redirect&bpo=1311): Under Windows, the `nul` file now yields True via [`exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists) plus a legitimate [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) result carrying `S_IFCHR`.

[bpo-38081](https://bugs.python.org/issue?@action=redirect&bpo=38081): Prevent error calling [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) on `'NUL'`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
