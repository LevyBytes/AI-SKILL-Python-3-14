# Python 3.8.0 beta 1 / library / shutil

[bpo-24564](https://bugs.python.org/issue?@action=redirect&bpo=24564): [`shutil.copystat()`](https://docs.python.org/3.14/library/shutil.html#shutil.copystat) henceforth disregards [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL) from [`os.setxattr()`](https://docs.python.org/3.14/library/os.html#os.setxattr), which can crop up while copying files onto filesystems lacking extended-attribute support.

Giampaolo Rodola supplied the original patch, and Ying Wang refreshed it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
