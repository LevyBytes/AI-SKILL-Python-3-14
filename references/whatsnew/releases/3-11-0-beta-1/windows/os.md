# Python 3.11.0 beta 1 / windows / os

[bpo-46785](https://bugs.python.org/issue?@action=redirect&bpo=46785): Settle the race condition between [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) and unlinking a file on Windows, by relying on the error codes that `FindFirstFileW()` returns where suitable inside `win32_xstat_impl`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
