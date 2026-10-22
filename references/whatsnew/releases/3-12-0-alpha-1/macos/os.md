# Python 3.12.0 alpha 1 / macos / os

[gh-97897](https://github.com/python/cpython/issues/97897): The `mkfifoat` and `mknodat` system calls are supported by the macOS 13 SDK. Passing the `dir_fd` option to either [`os.mkfifo()`](https://docs.python.org/3.14/library/os.html#os.mkfifo) or [`os.mknod()`](https://docs.python.org/3.14/library/os.html#os.mknod) might segfault when cpython was compiled against the macOS 13 SDK yet executed on an older macOS release. To guard against that, runtime detection of these system calls ("weaklinking") was added, matching the approach taken for other recent macOS syscalls.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
