# shutil — Platform-dependent efficient copy operations

### Platform-dependent efficient copy operations

As of Python 3.8, every function that performs a file copy (`copyfile()`, `copy()`, `copy2()`, `copytree()`, and `move()`) may employ platform-specific "fast-copy" syscalls so the file copies more efficiently (see [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671)). "fast-copy" signifies that the copy happens inside the kernel, sidestepping the userspace buffers Python would otherwise use as in "`outfd.write(infd.read())`".

On macOS [fcopyfile](http://www.manpagez.com/man/3/copyfile/) is used to copy the file content (not metadata).

On Linux [`os.copy_file_range()`](https://docs.python.org/3.14/library/os.html#os.copy_file_range) or [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) is used.

On Solaris [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile) is used.

On Windows, a larger default buffer (1 MiB rather than 64 KiB) is adopted by `shutil.copyfile()`, together with a [`memoryview()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview)-based form of `shutil.copyfileobj()`.

Should the fast-copy operation fail with no data yet written to the destination file, shutil quietly reverts to the less efficient `copyfileobj()` function internally.

Changed in version 3.8.

Changed in version 3.14: Solaris now uses [`os.sendfile()`](https://docs.python.org/3.14/library/os.html#os.sendfile).

Changed in version 3.14: Where a Linux filesystem supports it, [`os.copy_file_range()`](https://docs.python.org/3.14/library/os.html#os.copy_file_range) may internally drive a copy-on-write or server-side copy.

[Subject index](INDEX.md) · [Previous](shutil-chown-to-shutil-error.md) · [Continue](copytree-example.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
