# Python 3.11.0 alpha 1 / core and builtins / posix

[bpo-43895](https://bugs.python.org/issue?@action=redirect&bpo=43895): A stale internal cache of shared object file handles, dating to 1995, has been deleted from dynload_shlib.c. It tried — though without any guarantee — to keep a .so from being dlopen'ed twice, a workaround for defects in mid-1990s posix-ish operating systems.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
