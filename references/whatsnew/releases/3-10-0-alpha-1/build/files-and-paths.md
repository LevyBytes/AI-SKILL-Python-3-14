# Python 3.10.0 alpha 1 / build / files and paths

[bpo-41617](https://bugs.python.org/issue?@action=redirect&bpo=41617): Patch the `pycore_bitutils.h` header file so it works with older clang releases: `__builtin_bswap16()` is missing from LLVM clang 3.0.

[bpo-40684](https://bugs.python.org/issue?@action=redirect&bpo=40684): When `./configure --with-platlibdir` is in effect, `make install` now applies the `PLATLIBDIR` variable to determine the destination `lib-dynload/` directory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
