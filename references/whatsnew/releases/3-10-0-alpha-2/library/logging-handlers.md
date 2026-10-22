# Python 3.10.0 alpha 2 / library / logging handlers

[bpo-26789](https://bugs.python.org/issue?@action=redirect&bpo=26789): To allow opening or reopening the file throughout Python finalization, the [`logging.FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler) class now retains a handle on the builtin [`open()`](https://docs.python.org/3.14/library/functions.html#open) function. This fixes failures such as: `NameError: name 'open' is not defined`. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
