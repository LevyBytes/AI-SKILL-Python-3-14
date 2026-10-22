# What's New In Python 3.7 / os — os

### os

[`os.fwalk()`](https://docs.python.org/3.14/library/os.html#os.fwalk) will now take its *path* argument as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). (Contributed by Serhiy Storchaka in [bpo-28682](https://bugs.python.org/issue?@action=redirect&bpo=28682).)

[`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) picked up support for [file descriptors](https://docs.python.org/3.14/library/os.html#path-fd). (Contributed by Serhiy Storchaka in [bpo-25996](https://bugs.python.org/issue?@action=redirect&bpo=25996).)

A new [`register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) function lets you register Python callbacks that run when a process forks. (Contributed by Antoine Pitrou in [bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

Added the [`os.preadv()`](https://docs.python.org/3.14/library/os.html#os.preadv) function (which merges what [`os.readv()`](https://docs.python.org/3.14/library/os.html#os.readv) and [`os.pread()`](https://docs.python.org/3.14/library/os.html#os.pread) do) together with [`os.pwritev()`](https://docs.python.org/3.14/library/os.html#os.pwritev) (which merges what [`os.writev()`](https://docs.python.org/3.14/library/os.html#os.writev) and [`os.pwrite()`](https://docs.python.org/3.14/library/os.html#os.pwrite) do). (Contributed by Pablo Galindo in [bpo-31368](https://bugs.python.org/issue?@action=redirect&bpo=31368).)

For [`os.makedirs()`](https://docs.python.org/3.14/library/os.html#os.makedirs), the mode argument no longer changes the permission bits on freshly created intermediate-level directories. (Contributed by Serhiy Storchaka in [bpo-19930](https://bugs.python.org/issue?@action=redirect&bpo=19930).)

[`os.dup2()`](https://docs.python.org/3.14/library/os.html#os.dup2) now hands back the new file descriptor. Earlier, it always gave `None`. (Contributed by Benjamin Peterson in [bpo-32441](https://bugs.python.org/issue?@action=redirect&bpo=32441).)

Under Solaris and the systems derived from it, the structure that [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) returns now carries the [`st_fstype`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_fstype) attribute. (Contributed by Jesús Cea Avión in [bpo-32659](https://bugs.python.org/issue?@action=redirect&bpo=32659).)

[Subject index](INDEX.md) · [Previous source section](multiprocessing.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
