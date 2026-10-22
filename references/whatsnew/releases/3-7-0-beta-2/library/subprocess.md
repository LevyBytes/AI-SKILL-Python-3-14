# Python 3.7.0 beta 2 / library / subprocess

[bpo-32777](https://bugs.python.org/issue?@action=redirect&bpo=32777): Corrected an uncommon yet possible pre-exec deadlock of a child process in subprocess across POSIX systems while flagging file descriptors as inheritable on exec inside the child process. The bug looks to have arrived back in 3.4.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
