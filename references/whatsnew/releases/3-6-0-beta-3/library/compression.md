# Python 3.6.0 beta 3 / library / compression

[bpo-28449](https://bugs.python.org/issue?@action=redirect&bpo=28449): When called with mode "r" or "r:", tarfile.open() now first attempts to open a tar file with compression before attempting it without. Failing that, it stood a 50% chance of failing when ignore_zeros=True.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
