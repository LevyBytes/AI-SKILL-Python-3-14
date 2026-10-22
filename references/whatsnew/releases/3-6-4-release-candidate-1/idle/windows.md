# Python 3.6.4 release candidate 1 / idle / windows

[bpo-31858](https://bugs.python.org/issue?@action=redirect&bpo=31858): IDLE ? Confine shell prompt manipulation strictly to the shell. The editor and output windows only ever observe an empty final prompt line. This trims the code and corrects a small bug arising when a newline is inserted. Sys.ps1, when present, is read during Shell start-up, yet it is neither set nor altered.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
