# Python 3.6.5 release candidate 1 / library / subprocess

[bpo-32777](https://bugs.python.org/issue?@action=redirect&bpo=32777): Closed an uncommon yet possible pre-exec deadlock in the subprocess child on POSIX when the child marks file descriptors inheritable during exec. The defect seems to date back to 3.4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
