# Python 3.6.0 alpha 1 / library / os

[bpo-26735](https://bugs.python.org/issue?@action=redirect&bpo=26735): Corrected [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) on Solaris 11.3 and later when asked for more than 1,024 bytes: it now invokes `getrandom()` repeatedly, capping each call at 1024 bytes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
