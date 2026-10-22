# Python 3.14.0 alpha 1 / library / fcntl

[gh-69214](https://github.com/python/cpython/issues/69214): Correct the *request* parameter of `fcntl.ioctl()`: it now takes an `unsigned long` in place of an `unsigned int` for the *request* parameter of [`fcntl.ioctl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.ioctl), allowing requests above `UINT_MAX`. Victor Stinner authored the patch.

[gh-116622](https://github.com/python/cpython/issues/116622): Under Android, [`fcntl`](https://docs.python.org/3.14/library/fcntl.html#module-fcntl) no longer surfaces the `FICLONE` and `FICLONERANGE` constants, since SELinux blocks those ioctls.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
