# Python 3.6.0 beta 2 / core and builtins / fall back reading dev urandom device whenever getrandom syscall

[bpo-27955](https://bugs.python.org/issue?@action=redirect&bpo=27955): Fall back to reading the /dev/urandom device whenever the getrandom() syscall returns EPERM, for instance when SECCOMP blocks it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
