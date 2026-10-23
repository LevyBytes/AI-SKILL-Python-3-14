# What's New In Python 3.3 / shutil - os, shutil

### shutil

- New functions:

  - [`disk_usage()`](https://docs.python.org/3.14/library/shutil.html#shutil.disk_usage): provides total, used and free disk space statistics. (Contributed by Giampaolo Rodol?? in [bpo-12442](https://bugs.python.org/issue?@action=redirect&bpo=12442).)

  - [`chown()`](https://docs.python.org/3.14/library/shutil.html#shutil.chown): lets you reassign the owning user and/or group of a given path by naming the user/group, not just supplying their numeric ids. (Contributed by Sandro Tosi in [bpo-12191](https://bugs.python.org/issue?@action=redirect&bpo=12191).)

  - [`shutil.get_terminal_size()`](https://docs.python.org/3.14/library/shutil.html#shutil.get_terminal_size): hands back the dimensions of the terminal window the interpreter is connected to. (Contributed by Zbigniew Jędrzejewski-Szmek in [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609).)

- On platforms with the capability, [`copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) and [`copystat()`](https://docs.python.org/3.14/library/shutil.html#shutil.copystat) now retain file timestamps at nanosecond resolution. On Linux they additionally retain a file's "extended attributes". (Contributed by Larry Hastings in [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127) and [bpo-15238](https://bugs.python.org/issue?@action=redirect&bpo=15238).)

- A number of functions now accept an optional `symlinks` argument: with that flag set true, symlinks stay undereferenced and the work happens on the symlink itself (or a new symlink is produced, where applicable). (Contributed by Hynek Schlawack in [bpo-12715](https://bugs.python.org/issue?@action=redirect&bpo=12715).)

- While shifting files onto a separate file system, [`move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) now treats symlinks the same way the posix `mv` command would, rebuilding the symlink instead of duplicating the target file's contents. (Contributed by Jonathan Niehof in [bpo-9993](https://bugs.python.org/issue?@action=redirect&bpo=9993).) On top of that, `move()` now hands back the `dst` argument as what it returns.

- [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) now withstands symlink attacks on whichever platforms offer the new `dir_fd` parameter in [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) and [`os.unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink). (Contributed by Martin von Löwis and Hynek Schlawack in [bpo-4489](https://bugs.python.org/issue?@action=redirect&bpo=4489).)

[Subject index](INDEX.md) · [Previous source section](shlex.md) · [Next source section](signal.md) · [Release/subject declaration](summary-release-highlights.md)
