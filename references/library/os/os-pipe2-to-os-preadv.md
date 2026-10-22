# os: Pipes, file allocation, access advice and positional reads

Build a pipe. The call hands back a pair of file descriptors `(r, w)`, the first for reading and the second for writing. By default the freshly created descriptor is non-inheritable.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.4: The descriptors produced here are now non-inheritable.

 os.pipe2(*flags*, */*)

Build a pipe atomically with *flags* applied. You assemble *flags* by combining one or more of these constants with OR: `O_NONBLOCK`, `O_CLOEXEC`. The call hands back a pair of file descriptors `(r, w)`, the first for reading and the second for writing.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.3.

 os.posix_fallocate(*fd*, *offset*, *len*, */*)

Guarantees that the file identified by *fd* has sufficient disk space reserved, beginning at *offset* and extending across *len* bytes.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.posix_fadvise(*fd*, *offset*, *len*, *advice*, */*)

Signals that data will be accessed in a particular pattern, which lets the kernel apply optimizations. The hint covers the portion of the file identified by *fd* that begins at *offset* and spans *len* bytes. *advice* is one of `POSIX_FADV_NORMAL`, `POSIX_FADV_SEQUENTIAL`, `POSIX_FADV_RANDOM`, `POSIX_FADV_NOREUSE`, `POSIX_FADV_WILLNEED` or `POSIX_FADV_DONTNEED`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.POSIX_FADV_NORMAL

 os.POSIX_FADV_SEQUENTIAL

 os.POSIX_FADV_RANDOM

 os.POSIX_FADV_NOREUSE

 os.POSIX_FADV_WILLNEED

 os.POSIX_FADV_DONTNEED

Constants suitable for the *advice* argument of `posix_fadvise()`, each declaring the access pattern expected to occur.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.pread(*fd*, *n*, *offset*, */*)

Read up to *n* bytes from file descriptor *fd* at position *offset*, while keeping the file offset where it was.

A bytestring holding the bytes that were read is returned. When the file referenced by *fd* has reached its end, the call yields an empty bytes object.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.posix_openpt(*oflag*, */*)

Open a master pseudo-terminal device and give back a file descriptor for it.

Invokes the `posix_openpt()` function of the C standard library. The *oflag* argument configures the file status flags and file access modes described in your platform's manual page for `posix_openpt()`.

The descriptor handed back is non-inheritable. When `O_CLOEXEC` exists on the system, that value is merged into *oflag*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.13.

 os.preadv(*fd*, *buffers*, *offset*, *flags=0*, */*)

Read from file descriptor *fd* at position *offset* into a set of mutable [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *buffers*, while keeping the file offset where it was. Each buffer is filled completely before the call proceeds to the following buffer in the sequence to store the remaining data.

The flags argument holds a bitwise OR of zero or more of the flags below:

-

[Subject index](INDEX.md) · [Continue](os-rwf-nowait-to-os-pwritev.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md) · [Owning module, declaration or section: os.pipe](os-o-evtonly-to-os-pipe.md) · [Preceding source contract and version conditions](os-o-evtonly-to-os-pipe.md)
