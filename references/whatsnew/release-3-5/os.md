# What’s New In Python 3.5 / os - os, os.path

### os

There is a new [`scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) function that hands back an iterator over [`DirEntry`](https://docs.python.org/3.14/library/os.html#os.DirEntry) objects. Where it can, `scandir()` pulls file attributes during the directory walk, so follow-up system calls to learn a file's type or attributes become unnecessary, which can boost performance considerably. (Contributed by Ben Hoyt with the help of Victor Stinner in [bpo-22524](https://bugs.python.org/issue?@action=redirect&bpo=22524).)

A new [`stat_result.st_file_attributes`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_file_attributes) attribute is now provided on Windows. It maps to the `dwFileAttributes` member of the `BY_HANDLE_FILE_INFORMATION` structure that `GetFileInformationByHandle()` hands back. (Contributed by Ben Hoyt in [bpo-21719](https://bugs.python.org/issue?@action=redirect&bpo=21719).)

On Linux 3.17 and later the [`urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) function now relies on the `getrandom()` syscall, and on OpenBSD 5.6 and later it uses `getentropy()`, which drops the dependence on `/dev/urandom` and sidesteps breakage caused by possible file descriptor exhaustion. (Contributed by Victor Stinner in [bpo-22181](https://bugs.python.org/issue?@action=redirect&bpo=22181).)

Reading and changing a file descriptor's blocking mode ([`O_NONBLOCK`](https://docs.python.org/3.14/library/os.html#os.O_NONBLOCK)) is now possible with the new [`get_blocking()`](https://docs.python.org/3.14/library/os.html#os.get_blocking) and [`set_blocking()`](https://docs.python.org/3.14/library/os.html#os.set_blocking) functions. (Contributed by Victor Stinner in [bpo-22054](https://bugs.python.org/issue?@action=redirect&bpo=22054).)

Windows now provides the [`truncate()`](https://docs.python.org/3.14/library/os.html#os.truncate) and [`ftruncate()`](https://docs.python.org/3.14/library/os.html#os.ftruncate) functions. (Contributed by Steve Dower in [bpo-23668](https://bugs.python.org/issue?@action=redirect&bpo=23668).)

A new [`os.path.commonpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.commonpath) function hands back the longest common sub-path across the pathnames it is given. In contrast to the [`os.path.commonprefix()`](https://docs.python.org/3.14/library/os.path.html#os.path.commonprefix) function, the result is always a valid path:

```python
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'

>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'

```

(Contributed by Rafik Draoui and Serhiy Storchaka in [bpo-10395](https://bugs.python.org/issue?@action=redirect&bpo=10395).)

[Subject index](INDEX.md) · [Previous source section](operator.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
