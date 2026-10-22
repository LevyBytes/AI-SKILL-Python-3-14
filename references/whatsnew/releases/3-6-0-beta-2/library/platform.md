# Python 3.6.0 beta 2 / library / platform

[bpo-28148](https://bugs.python.org/issue?@action=redirect&bpo=28148): The time module no longer calls localtime() or gmtime(). A platform-independent _PyTime_localtime API was introduced, modeled on POSIX localtime_r yet present everywhere. Ed Schouten contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
