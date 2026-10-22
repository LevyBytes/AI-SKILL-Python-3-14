# Python 3.5.2 release candidate 1 / library / fcntl

[bpo-27057](https://bugs.python.org/issue?@action=redirect&bpo=27057): Fix os.set_inheritable() on Android, where ioctl() is blocked by SELinux and returns EACCESS. The routine now drops back to fcntl(). Micha?? Bednarski authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
