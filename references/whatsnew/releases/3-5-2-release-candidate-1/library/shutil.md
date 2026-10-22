# Python 3.5.2 release candidate 1 / library / shutil

[bpo-26801](https://bugs.python.org/issue?@action=redirect&bpo=26801): Repair the error handling within [`shutil.get_terminal_size()`](https://docs.python.org/3.14/library/shutil.html#shutil.get_terminal_size) so it catches [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) in place of [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError). Emanuel Barry authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
