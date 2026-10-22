# os: `os.RWF_DSYNC`, `os.RWF_SYNC`, `os.RWF_APPEND`, `os.read()`, `os.readinto()`

`RWF_APPEND`

The grand total of bytes actually written is returned.

A ceiling on how many buffers may be supplied can be imposed by the operating system (the `sysconf()` value `'SC_IOV_MAX'`).

Merge the behavior of `os.writev()` together with `os.pwrite()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.

Using flags requires Linux >= 4.6.

Added in version 3.7.

 os.RWF_DSYNC

Supplies a per-write counterpart of the `O_DSYNC` `os.open()` flag. The effect of this flag reaches only the data range that the system call wrote.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.7.

Added in version 3.7.

 os.RWF_SYNC

Supplies a per-write counterpart of the `O_SYNC` `os.open()` flag. The effect of this flag reaches only the data range that the system call wrote.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.7.

Added in version 3.7.

 os.RWF_APPEND

Supplies a per-write counterpart of the `O_APPEND` `os.open()` flag. This flag carries meaning only for `os.pwritev()`, and its effect reaches only the data range that the system call wrote. The *offset* argument has no bearing on the write operation; data always lands at the end of the file. Yet, when the *offset* argument is `-1`, the current file *offset* gets refreshed.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.16.

Added in version 3.10.

 os.read(*fd*, *n*, */*)

Read up to *n* bytes from file descriptor *fd*.

A bytestring holding the bytes that were read is returned. When the file referenced by *fd* has reached its end, the call yields an empty bytes object.

Note

This routine targets low-level I/O and is meant for a file descriptor such as one produced by `os.open()` or `pipe()`. When you want to read a "file object" produced by the built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open), by `popen()`, or by `fdopen()`, or [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), reach instead for its [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) or [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) methods.

Changed in version 3.5: When the system call is interrupted and the signal handler raises no exception, the routine now repeats the system call rather than raising an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 os.readinto(*fd*, *buffer*, */*)

Read from file descriptor *fd* into a mutable [buffer object](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) *buffer*.

The *buffer* must be mutable and [bytes-like](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). When it succeeds, the count of bytes read is returned. Fewer bytes than the buffer's size may come back. Should a signal interrupt the underlying system call, it is retried, unless the signal handler raises an exception. Errors of other kinds are not retried and an error is raised.

Returns 0 when *fd* sits at end of file or when the supplied *buffer* is of length 0 (a fact that can serve to probe for errors without actually reading data). The result is never negative.

Note

This routine targets low-level I/O and is meant for a file descriptor such as one produced by `os.open()` or `os.pipe()`. When you want to read a "file object" produced by the built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open), or [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), reach instead for its member functions, for instance [`io.BufferedIOBase.readinto()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.readinto), [`io.BufferedIOBase.read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read), or [`io.TextIOBase.read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read)

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](os-rwf-nowait-to-os-pwritev.md) · [Continue](os-sendfile-to-os-set-blocking.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
