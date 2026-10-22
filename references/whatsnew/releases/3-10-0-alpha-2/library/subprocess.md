# Python 3.10.0 alpha 2 / library / subprocess

[bpo-42146](https://bugs.python.org/issue?@action=redirect&bpo=42146): Plug a memory leak inside [`subprocess.Popen()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) for the case where a uid (gid) given in `user` (`group`, `extra_groups`) overflows `uid_t` (`gid_t`).

[bpo-35823](https://bugs.python.org/issue?@action=redirect&bpo=35823): On Linux, rely on `vfork()` over `fork()` for [`subprocess.Popen()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) to boost performance wherever it is judged safe.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
