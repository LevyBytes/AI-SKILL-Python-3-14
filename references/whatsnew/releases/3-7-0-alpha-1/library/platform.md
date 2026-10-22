# Python 3.7.0 alpha 1 / library / platform

[bpo-28148](https://bugs.python.org/issue?@action=redirect&bpo=28148): Quit relying on localtime() and gmtime() within the time module. A platform-independent _PyTime_localtime API, comparable to POSIX localtime_r yet present everywhere, was introduced. Ed Schouten supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
