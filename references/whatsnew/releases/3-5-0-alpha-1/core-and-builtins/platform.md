# Python 3.5.0 alpha 1 / core and builtins / platform

[bpo-22258](https://bugs.python.org/issue?@action=redirect&bpo=22258): Repaired the internal function set_inheritable() on Illumos. That platform exposes the function `ioctl(FIOCLEX)`, yet invoking it fails with errno set to ENOTTY: "Inappropriate ioctl for device". set_inheritable() now drops back to the slower `fcntl()` (`F_GETFD` and then `F_SETFD`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
