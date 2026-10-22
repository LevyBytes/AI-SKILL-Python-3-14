# What's New In Python 3.7 / locale — locale

### locale

A new *monetary* argument on [`locale.format_string()`](https://docs.python.org/3.14/library/locale.html#locale.format_string) lets the conversion apply monetary thousands separators along with grouping strings. (Contributed by Garvit in [bpo-10379](https://bugs.python.org/issue?@action=redirect&bpo=10379).)

The [`locale.getpreferredencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) function will now consistently hand back `'UTF-8'` under Android, or whenever the forced UTF-8 mode is active.

### locale

The `locale.format()` function is now deprecated; reach for [`locale.format_string()`](https://docs.python.org/3.14/library/locale.html#locale.format_string) instead. (Contributed by Garvit in [bpo-10379](https://bugs.python.org/issue?@action=redirect&bpo=10379).)

[Subject index](INDEX.md) · [Previous source section](itertools.md) · [Next source section](logging.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](importlib.md) · [Next source section](macpath.md)
