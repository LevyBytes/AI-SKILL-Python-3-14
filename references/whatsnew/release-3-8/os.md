# What’s New In Python 3.8 / os - ctypes, os

> (Contributed by Victor Stinner in [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).)

### os

A fresh [`add_dll_directory()`](https://docs.python.org/3.14/library/os.html#os.add_dll_directory) function has been added on Windows; it supplies extra search paths for native dependencies whenever you import extension modules or load DLLs by way of [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes).
> (Contributed by Steve Dower in [bpo-36085](https://bugs.python.org/issue?@action=redirect&bpo=36085).)

A fresh [`os.memfd_create()`](https://docs.python.org/3.14/library/os.html#os.memfd_create) function has been added to wrap the `memfd_create()` syscall.
> (Contributed by Zackery Spytz and Christian Heimes in [bpo-26836](https://bugs.python.org/issue?@action=redirect&bpo=26836).)

Under Windows, a large share of the hand-rolled code that dealt with reparse points (symlinks and directory junctions among them) is now deferred to the OS. Concretely, [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) henceforth follows whatever the platform supports, whereas [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) opens only those reparse points reporting themselves as "name surrogates"; the rest get opened just as `os.stat()` would. Across every scenario, [`os.stat_result.st_mode`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_mode) sets `S_IFLNK` exclusively for symbolic links rather than for any other variety of reparse point. When you need to recognize a different reparse-point kind, consult the freshly added [`os.stat_result.st_reparse_tag`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_reparse_tag) attribute.

Under Windows, [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) can henceforth read directory junctions. Be aware that [`islink()`](https://docs.python.org/3.14/library/os.path.html#os.path.islink) reports `False` for directory junctions, so logic that tests `islink` up front keeps treating junctions as if they were directories, whereas logic catching errors raised by `os.readlink()` might now regard junctions as links.

(Contributed by Steve Dower in [bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

[Subject index](INDEX.md) · [Previous source section](multiprocessing.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](os-path.md)
