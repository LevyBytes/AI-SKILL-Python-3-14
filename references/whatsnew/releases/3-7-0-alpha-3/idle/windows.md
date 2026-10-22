# Python 3.7.0 alpha 3 / idle / windows

[bpo-31858](https://bugs.python.org/issue?@action=redirect&bpo=31858): IDLE ? Confine shell prompt manipulation to the shell alone. Output and editor windows only ever observe a blank last prompt line. This trims the code and corrects a small bug arising when a newline is inserted. Sys.ps1, where it exists, is read at Shell start-up, yet is neither set nor altered.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
