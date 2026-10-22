# os: `os.close()`, `os.closerange()`, `os.copy_file_range()`, `os.device_encoding()`, `os.dup()`, `os.dup2()`

### File Descriptor Operations

These functions act on I/O streams that are referred to by file descriptors.

File descriptors are small integers that correspond to a file the current process has opened. By way of example, standard input is generally file descriptor 0, standard output is 1, and standard error is 2. Any further files a process opens then receive 3, 4, 5, and onward. The label "file descriptor" is a touch misleading; on Unix platforms, sockets and pipes are referred to by file descriptors as well.

When you need the file descriptor that goes with a [file object](https://docs.python.org/3.14/glossary.html#term-file-object), the [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method will fetch it. Bear in mind that working with the file descriptor directly sidesteps the file object methods, skipping over things like the internal buffering of data.

 os.close(*fd*)

Close file descriptor *fd*.

Note

This function is meant for low-level I/O and must target a file descriptor of the kind `os.open()` or `pipe()` hands back. When you instead have a "file object" produced by the built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open) or by `popen()` or `fdopen()`, close it by calling its [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) method.

 os.closerange(*fd_low*, *fd_high*, */*)

Close every file descriptor from *fd_low* (inclusive) through *fd_high* (exclusive), ignoring errors. Equivalent to (yet far faster than):

```python
for fd in range(fd_low, fd_high):
    try:
        os.close(fd)
    except OSError:
        pass

```

 os.copy_file_range(*src*, *dst*, *count*, *offset_src=None*, *offset_dst=None*)

Copy *count* bytes out of file descriptor *src*, beginning at offset *offset_src*, into file descriptor *dst*, beginning at offset *offset_dst*. When *offset_src* is `None`, *src* is read from its current position; the same goes for *offset_dst*.

On Linux kernels older than 5.3, the files that *src* and *dst* point to have to live on the same filesystem, otherwise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised with [`errno`](https://docs.python.org/3.14/library/exceptions.html#OSError.errno) set to [`errno.EXDEV`](https://docs.python.org/3.14/library/errno.html#errno.EXDEV).

This copy happens without the extra cost of shuttling data from the kernel out to user space and then back into the kernel. On top of that, some filesystems may add further optimizations, like the use of reflinks (that is, two or more inodes sharing pointers to the same copy-on-write disk blocks; btrfs and XFS are among the supported file systems) and server-side copy (as with NFS).

Bytes get copied by the function from one file descriptor to another. Any text options, such as the encoding and the line ending, play no part.

What comes back is the count of bytes copied. This may be fewer than the count requested.

Note

On Linux, `os.copy_file_range()` should not be used to copy a range of a pseudo file out of a special filesystem like procfs and sysfs. Owing to a known Linux kernel issue, it will always copy no bytes and give back 0 as though the file were empty.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.5 with glibc >= 2.27.

Added in version 3.8.

 os.device_encoding(*fd*)

Give back a string describing the encoding of the device tied to *fd* when it is connected to a terminal; otherwise give back [`None`](https://docs.python.org/3.14/library/constants.html#None).

On Unix, when the Python UTF-8 Mode is on, give back `'UTF-8'` rather than the device encoding.

Changed in version 3.10: On Unix, the Python UTF-8 Mode is now honored by the function.

 os.dup(*fd*, */*)

Give back a copy of file descriptor *fd*. That fresh file descriptor is non-inheritable.

On Windows, when you copy a standard stream (0: stdin, 1: stdout, 2: stderr), the resulting file descriptor turns out inheritable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

Changed in version 3.4: From here on the fresh file descriptor is non-inheritable.

 os.dup2(*fd*, *fd2*, *inheritable=True*)

Duplicate file descriptor *fd* onto *fd2*, closing the latter beforehand if it must. Give back *fd2*. The new file descriptor comes out inheritable by default, or non-inheritable when *inheritable* is `False`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

Changed in version 3.4: The optional *inheritable* parameter was added.

Changed in version 3.7: On success *fd2* is returned. Beforehand, `None` came back every time.

[Subject index](INDEX.md) · [Previous](os-fdopen.md) · [Continue](os-fchmod-to-os-ftruncate.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
