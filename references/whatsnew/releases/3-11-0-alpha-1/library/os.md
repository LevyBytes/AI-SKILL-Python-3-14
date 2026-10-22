# Python 3.11.0 alpha 1 / library / os

[bpo-44849](https://bugs.python.org/issue?@action=redirect&bpo=44849): Repaired the [`os.set_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_inheritable) function on FreeBSD 14 for a file descriptor opened under the [`O_PATH`](https://docs.python.org/3.14/library/os.html#os.O_PATH) flag: skip the [`EBADF`](https://docs.python.org/3.14/library/errno.html#errno.EBADF) error from `ioctl()` and drop back to the `fcntl()` implementation. Victor Stinner wrote this patch.

[bpo-44219](https://bugs.python.org/issue?@action=redirect&bpo=44219): Drop the GIL while running `isatty` system calls against arbitrary file descriptors. This notably touches [`os.isatty()`](https://docs.python.org/3.14/library/os.html#os.isatty), [`os.device_encoding()`](https://docs.python.org/3.14/library/os.html#os.device_encoding) and [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper). As a knock-on effect, [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) in text mode feels it too. The change resolves a deadlock within `os.isatty()`. Vincent Michel wrote the patch in [bpo-44219](https://bugs.python.org/issue?@action=redirect&bpo=44219).

[bpo-44611](https://bugs.python.org/issue?@action=redirect&bpo=44611): On Windows, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom): now calls the BCryptGenRandom API rather than the CryptGenRandom API, the latter being deprecated within the Microsoft Windows API. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
