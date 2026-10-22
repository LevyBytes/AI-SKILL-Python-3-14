# Python 3.6.0 alpha 1 / library / fcntl

[bpo-27057](https://bugs.python.org/issue?@action=redirect&bpo=27057): Repair os.set_inheritable() on Android, where SELinux blocks ioctl() and it fails with EACCESS. The function now falls back to fcntl(). Micha?? Bednarski wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
