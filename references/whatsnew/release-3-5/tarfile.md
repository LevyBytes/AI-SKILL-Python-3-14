# What’s New In Python 3.5 / tarfile — tarfile

### tarfile

To ask for exclusive creation, the *mode* argument of the [`open()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.open) function now takes `"x"`. Berker Peksag landed this (see [bpo-21717](https://bugs.python.org/issue?@action=redirect&bpo=21717)).

A *numeric_owner* keyword argument is now accepted by the [`TarFile.extractall()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extractall) and [`TarFile.extract()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.extract) methods. With it set to `True`, the files and directories that get extracted take their ownership from the numeric `uid` and `gid` stored in the tarfile. When left `False` — the default, matching how releases before 3.5 behaved — ownership comes from the user and group named inside the tarfile. Michael Vogt and Eric Smith added this (see [bpo-23193](https://bugs.python.org/issue?@action=redirect&bpo=23193)).

An optional *members* keyword argument is now taken by the [`TarFile.list()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.list); it may hold any subset of what [`TarFile.getmembers()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.getmembers) returns. Serhiy Storchaka contributed this (see [bpo-21549](https://bugs.python.org/issue?@action=redirect&bpo=21549)).

[Subject index](INDEX.md) · [Previous source section](sysconfig.md) · [Next source section](threading.md) · [Release/subject declaration](summary-release-highlights.md)
