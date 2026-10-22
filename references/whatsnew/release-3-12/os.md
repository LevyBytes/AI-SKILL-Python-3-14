# What’s New In Python 3.12 / os — os

### os

- Add [`os.PIDFD_NONBLOCK`](https://docs.python.org/3.14/library/os.html#os.PIDFD_NONBLOCK) for opening a process file descriptor through [`os.pidfd_open()`](https://docs.python.org/3.14/library/os.html#os.pidfd_open) in non-blocking mode. (Contributed by Kumar Aditya in [gh-93312](https://github.com/python/cpython/issues/93312).)

- [`os.DirEntry`](https://docs.python.org/3.14/library/os.html#os.DirEntry) picked up an [`os.DirEntry.is_junction()`](https://docs.python.org/3.14/library/os.html#os.DirEntry.is_junction) method for testing whether the entry happens to be a junction. (Contributed by Charles Machalow in [gh-99547](https://github.com/python/cpython/issues/99547).)

- Add the [`os.listdrives()`](https://docs.python.org/3.14/library/os.html#os.listdrives), [`os.listvolumes()`](https://docs.python.org/3.14/library/os.html#os.listvolumes) and [`os.listmounts()`](https://docs.python.org/3.14/library/os.html#os.listmounts) functions on Windows that enumerate drives, volumes and mount points. (Contributed by Steve Dower in [gh-102519](https://github.com/python/cpython/issues/102519).)

- On Windows, [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) and [`os.lstat()`](https://docs.python.org/3.14/library/os.html#os.lstat) deliver greater accuracy. The `st_birthtime` field now carries the file’s creation time, while `st_ctime` is deprecated yet still reports the creation time (though a later release will hand back the last metadata change, to line up with other platforms). Depending on the file system, `st_dev` can reach 64 bits and `st_ino` can reach 128 bits, and `st_rdev` is fixed at zero in place of bogus values. The pair may run noticeably faster on more recent Windows builds. (Contributed by Steve Dower in [gh-99726](https://github.com/python/cpython/issues/99726).)

[Subject index](INDEX.md) · [Previous source section](math.md) · [Next source section](os-path.md) · [Release/subject declaration](summary-release-highlights.md)
