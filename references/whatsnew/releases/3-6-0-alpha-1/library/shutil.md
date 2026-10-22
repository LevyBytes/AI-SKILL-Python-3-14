# Python 3.6.0 alpha 1 / library / shutil

[bpo-26801](https://bugs.python.org/issue?@action=redirect&bpo=26801): Corrected error handling within [`shutil.get_terminal_size()`](https://docs.python.org/3.14/library/shutil.html#shutil.get_terminal_size) so it now traps [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) in place of [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError). Emanuel Barry wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
