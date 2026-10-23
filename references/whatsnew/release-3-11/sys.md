# What's New In Python 3.11 / sys - sys

### sys

- The `type` and `traceback` fields are now derived by [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) from the `value` (the exception instance). Consequently, editing an exception mid-handling causes those edits to surface on later `exc_info()` calls. (Contributed by Irit Katriel in [bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711).)

- [`sys.exception()`](https://docs.python.org/3.14/library/sys.html#sys.exception) was added; it hands back the live exception instance (the same as `sys.exc_info()[1]`). (Contributed by Irit Katriel in [bpo-46328](https://bugs.python.org/issue?@action=redirect&bpo=46328).)

- The [`sys.flags.safe_path`](https://docs.python.org/3.14/library/sys.html#sys.flags) flag was added. (Contributed by Victor Stinner in [gh-57684](https://github.com/python/cpython/issues/57684).)

[Subject index](INDEX.md) · [Previous source section](string.md) · [Next source section](sysconfig.md) · [Release/subject declaration](summary-release-highlights.md)
