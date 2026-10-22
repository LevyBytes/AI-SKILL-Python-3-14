# Python 3.8.0 alpha 1 / library / platform

[bpo-26544](https://bugs.python.org/issue?@action=redirect&bpo=26544): Repaired the implementation of [`platform.libc_ver()`](https://docs.python.org/3.14/library/platform.html#platform.libc_ver). For glibc it nearly always reported version '2.9'.

[bpo-35348](https://bugs.python.org/issue?@action=redirect&bpo=35348): Made the [`platform.architecture()`](https://docs.python.org/3.14/library/platform.html#platform.architecture) parsing of `file` command output sturdier: supply the `-b` option to the `file` command so the filename is dropped, pin the C locale, and additionally look for the "shared object" pattern.

[bpo-35346](https://bugs.python.org/issue?@action=redirect&bpo=35346): Withdraw Mac OS 9 plus Rhapsody support from the [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) module. The final Rhapsody release shipped in 2000. The final Mac OS 9 release shipped in 2001.

[bpo-35389](https://bugs.python.org/issue?@action=redirect&bpo=35389): [`platform.libc_ver()`](https://docs.python.org/3.14/library/platform.html#platform.libc_ver) now consults `os.confstr('CS_GNU_LIBC_VERSION')` when it is present and the *executable* parameter has not been provided.

[bpo-35346](https://bugs.python.org/issue?@action=redirect&bpo=35346): [`platform.uname()`](https://docs.python.org/3.14/library/platform.html#platform.uname) now sends `stderr` to [`os.devnull`](https://docs.python.org/3.14/library/os.html#os.devnull) while running external programs such as `cmd /c ver`.

[bpo-35344](https://bugs.python.org/issue?@action=redirect&bpo=35344): On macOS, [`platform.platform()`](https://docs.python.org/3.14/library/platform.html#platform.platform) now consults [`platform.mac_ver()`](https://docs.python.org/3.14/library/platform.html#platform.mac_ver), provided it yields a non-empty release string, to read the macOS version in place of the darwin version.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
