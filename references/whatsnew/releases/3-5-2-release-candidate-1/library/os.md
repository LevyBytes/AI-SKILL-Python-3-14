# Python 3.5.2 release candidate 1 / library / os

[bpo-26735](https://bugs.python.org/issue?@action=redirect&bpo=26735): Fix [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) on Solaris 11.3 and later when more than 1,024 bytes are requested: it now invokes `getrandom()` repeatedly, capped at 1024 bytes per call.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
