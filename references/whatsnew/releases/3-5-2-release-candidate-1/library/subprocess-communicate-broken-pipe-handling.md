# Python 3.5.2 release candidate 1 / library / subprocess popen communicate properly disregards brokenpipeerror more or all cases where

[bpo-26373](https://bugs.python.org/issue?@action=redirect&bpo=26373): subprocess.Popen.communicate now properly disregards BrokenPipeError in more (or all) cases where the child process exits before .communicate() runs.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
