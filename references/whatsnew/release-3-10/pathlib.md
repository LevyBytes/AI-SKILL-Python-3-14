# What's New In Python 3.10 / pathlib — os, pathlib

### pathlib

Add slice support to [`PurePath.parents`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parents). (Contributed by Joshua Cannon in [bpo-35498](https://bugs.python.org/issue?@action=redirect&bpo=35498).)

Add negative indexing support to [`PurePath.parents`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parents). (Contributed by Yaroslav Pankovych in [bpo-21041](https://bugs.python.org/issue?@action=redirect&bpo=21041).)

Add [`Path.hardlink_to`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.hardlink_to) method that supersedes `link_to()`. This replacement keeps the same argument order found in [`symlink_to()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.symlink_to). (Contributed by Barney Gale in [bpo-39950](https://bugs.python.org/issue?@action=redirect&bpo=39950).)

[`pathlib.Path.stat()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.stat) and [`chmod()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.chmod) now take a *follow_symlinks* keyword-only argument so they line up with the matching functions in the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module. (Contributed by Barney Gale in [bpo-39906](https://bugs.python.org/issue?@action=redirect&bpo=39906).)

[Subject index](INDEX.md) · [Previous source section](os-path.md) · [Next source section](platform.md) · [Release/subject declaration](summary-release-highlights.md)
