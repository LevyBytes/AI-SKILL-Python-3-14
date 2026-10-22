# os: `os.RWF_NOWAIT`, `os.RWF_HIPRI`, `os.ptsname()`, `os.pwrite()`, `os.pwritev()`

`RWF_HIPRI`

- `RWF_NOWAIT`

The grand total of bytes actually read is returned, which may fall short of the combined capacity of all the objects.

A ceiling on how many buffers may be supplied can be imposed by the operating system (the `sysconf()` value `'SC_IOV_MAX'`).

Merge the behavior of `os.readv()` together with `os.pread()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.

Using flags requires Linux >= 4.6.

Added in version 3.7.

 os.RWF_NOWAIT

Refrain from waiting for data that is not ready right away. With this flag in effect, the system call comes back at once if it would otherwise have to fetch data from the backing storage or block on a lock.

When some data did get read successfully, the count of bytes read is returned. When nothing was read, the result is `-1` and errno is set to [`errno.EAGAIN`](https://docs.python.org/3.14/library/errno.html#errno.EAGAIN).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.14.

Added in version 3.7.

 os.RWF_HIPRI

High priority read/write. Lets block-based filesystems poll the device, which lowers latency at the cost of possibly consuming more resources.

For now, on Linux, this capability works only on a file descriptor that was opened with the `O_DIRECT` flag.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 4.6.

Added in version 3.7.

 os.ptsname(*fd*, */*)

Give back the name of the slave pseudo-terminal device tied to the master pseudo-terminal device that file descriptor *fd* points at. The file descriptor *fd* stays open if the call fails.

Invokes the reentrant C standard library function `ptsname_r()` when it exists; if not, it falls back to the C standard library function `ptsname()`, which carries no thread-safety guarantee.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.13.

 os.pwrite(*fd*, *str*, *offset*, */*)

Write the bytestring contained in *str* to file descriptor *fd* at position *offset*, while keeping the file offset where it was.

The count of bytes actually written is returned.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.pwritev(*fd*, *buffers*, *offset*, *flags=0*, */*)

Write the data held in *buffers* to file descriptor *fd* at offset *offset*, while keeping the file offset where it was. *buffers* has to be a sequence of [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). The buffers get handled in array order. The first buffer is written out in full before the second is reached, and so forth.

The flags argument holds a bitwise OR of zero or more of the flags below:

- `RWF_DSYNC`

- `RWF_SYNC`

-

[Subject index](INDEX.md) · [Previous](os-pipe2-to-os-preadv.md) · [Continue](os-rwf-dsync-to-os-readinto.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
