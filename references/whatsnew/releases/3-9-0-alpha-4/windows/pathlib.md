# Python 3.9.0 alpha 4 / windows / pathlib

[bpo-38883](https://bugs.python.org/issue?@action=redirect&bpo=38883): [`home()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.home) and [`expanduser()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.expanduser) under Windows now favor `USERPROFILE` and stop using `HOME`, which regular user accounts do not usually set. This restores parity with [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser), which began ignoring `HOME` in 3.8, see [bpo-36264](https://bugs.python.org/issue?@action=redirect&bpo=36264).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
