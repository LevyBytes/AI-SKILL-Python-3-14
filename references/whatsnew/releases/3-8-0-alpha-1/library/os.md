# Python 3.8.0 alpha 1 / library / os

[bpo-33871](https://bugs.python.org/issue?@action=redirect&bpo=33871): Corrected an integer overflow in [`os.readv()`](https://docs.python.org/3.14/library/os.html#os.readv), [`os.writev()`](https://docs.python.org/3.14/library/os.html#os.writev), [`os.preadv()`](https://docs.python.org/3.14/library/os.html#os.preadv) and [`os.pwritev()`](https://docs.python.org/3.14/library/os.html#os.pwritev) and in [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) carrying *headers* or *trailers* arguments (on BSD-based OSes and macOS).

[bpo-34384](https://bugs.python.org/issue?@action=redirect&bpo=34384): On Windows, [`os.readlink()`](https://docs.python.org/3.14/library/os.html#os.readlink) now takes [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) and [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects.

[bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537): [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) and [`os.posix_spawnp()`](https://docs.python.org/3.14/library/os.html#os.posix_spawnp) now have a *setsid* parameter.

[bpo-35674](https://bugs.python.org/issue?@action=redirect&bpo=35674): Introduced a fresh [`os.posix_spawnp()`](https://docs.python.org/3.14/library/os.html#os.posix_spawnp) function. Patch by Joannah Nanjekye.

[bpo-34530](https://bugs.python.org/issue?@action=redirect&bpo=34530): When the `PATH` environment variable is unset, `distutils.spawn.find_executable()` now falls back on [`os.defpath`](https://docs.python.org/3.14/library/os.html#os.defpath).

[bpo-35022](https://bugs.python.org/issue?@action=redirect&bpo=35022): The `__fspath__` method (drawn from [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike)) is now supported by [`unittest.mock.MagicMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.MagicMock).

[bpo-34652](https://bugs.python.org/issue?@action=redirect&bpo=34652): On Linux, [`os.lchmod()`](https://docs.python.org/3.14/library/os.html#os.lchmod) is guaranteed never to be defined.

[bpo-20104](https://bugs.python.org/issue?@action=redirect&bpo=20104): Better error handling plus a fixed reference leak in [`os.posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn).

[bpo-35345](https://bugs.python.org/issue?@action=redirect&bpo=35345): The `platform.popen` function is gone, having been deprecated since Python 3.3: rely on [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
