# What's New In Python 3.4 / filecmp — filecmp, os

### filecmp

A new [`clear_cache()`](https://docs.python.org/3.14/library/filecmp.html#filecmp.clear_cache) function lets you wipe the [`filecmp`](https://docs.python.org/3.14/library/filecmp.html#module-filecmp) comparison cache, which leans on [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) data to judge whether the file shifted since the last compare. That helps, say, when a file may have changed and been re-checked within a span shorter than the resolution of a given filesystem's file modification time field. (Contributed by Mark Levitt in [bpo-18149](https://bugs.python.org/issue?@action=redirect&bpo=18149).)

A new module attribute, [`DEFAULT_IGNORES`](https://docs.python.org/3.14/library/filecmp.html#filecmp.DEFAULT_IGNORES), holds the directory list that the [`dircmp()`](https://docs.python.org/3.14/library/filecmp.html#filecmp.dircmp) function takes by default for its *ignore* parameter. (Work by Eli Bendersky, tracked in [bpo-15442](https://bugs.python.org/issue?@action=redirect&bpo=15442).)

[Subject index](INDEX.md) · [Previous source section](email.md) · [Next source section](functools.md) · [Release/subject declaration](release-highlights.md)
