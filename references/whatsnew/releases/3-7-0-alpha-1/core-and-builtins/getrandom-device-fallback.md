# Python 3.7.0 alpha 1 / core and builtins / fall back reading dev urandom device whenever getrandom syscall

[bpo-27955](https://bugs.python.org/issue?@action=redirect&bpo=27955): Fall back to reading the /dev/urandom device whenever the getrandom() syscall fails with EPERM, such as when SECCOMP blocks it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
