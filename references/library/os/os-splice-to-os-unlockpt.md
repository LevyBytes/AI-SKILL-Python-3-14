# os: `os.splice()`, `os.SPLICE_F_MOVE`, `os.SPLICE_F_NONBLOCK`, `os.SPLICE_F_MORE`, `os.readv()`, `os.tcgetpgrp()`, `os.tcsetpgrp()`, `os.ttyname()`, `os.unlockpt()`

os.splice(*src*, *dst*, *count*, *offset_src=None*, *offset_dst=None*, *flags=0*)

Move *count* bytes out of file descriptor *src*, beginning at offset *offset_src*, into file descriptor *dst*, beginning at offset *offset_dst*.

You can adjust the splicing behaviour by supplying a *flags* value. Any of the variables below may be used, joined together with bitwise OR (the `|` operator):

- When `SPLICE_F_MOVE` is supplied, the kernel is requested to move pages instead of copying them, though pages may still end up copied if the kernel is unable to move them away from the pipe.

- When `SPLICE_F_NONBLOCK` is supplied, the kernel is requested not to block on I/O. This turns the splice pipe operations nonblocking, yet splice can still block, because the spliced file descriptors themselves may block.

- When `SPLICE_F_MORE` is supplied, it gives the kernel a hint that further data will arrive in a later splice.

A minimum of one of the file descriptors has to point at a pipe. When *offset_src* is `None`, then *src* is read starting from the current position; the same holds for *offset_dst*. The offset belonging to whichever file descriptor refers to a pipe must be `None`. The files referenced by *src* and *dst* have to live on the same filesystem; otherwise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised with [`errno`](https://docs.python.org/3.14/library/exceptions.html#OSError.errno) set to [`errno.EXDEV`](https://docs.python.org/3.14/library/errno.html#errno.EXDEV).

This copy avoids the extra expense of moving data from the kernel out to user space and then back into the kernel. On top of that, certain filesystems may add further optimizations. The copy proceeds as though both files were opened in binary mode.

On success, the call returns the count of bytes spliced to or from the pipe. A returned value of 0 indicates end of input. When *src* points at a pipe, this signals that no data was available to move, and blocking would make no sense because no writers are attached to the write end of the pipe.

See also

The *[splice(2)](https://manpages.debian.org/splice(2))* man page.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 2.6.17 with glibc >= 2.5

Added in version 3.10.

 os.SPLICE_F_MOVE

 os.SPLICE_F_NONBLOCK

 os.SPLICE_F_MORE

Added in version 3.10.

 os.readv(*fd*, *buffers*, */*)

Read from file descriptor *fd* into several mutable [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *buffers*. Each buffer is filled completely before the call proceeds to the following buffer in the sequence to store the remaining data.

The grand total of bytes actually read is returned, which may fall short of the combined capacity of all the objects.

A ceiling on how many buffers may be supplied can be imposed by the operating system (the `sysconf()` value `'SC_IOV_MAX'`).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.tcgetpgrp(*fd*, */*)

Give back the process group tied to the terminal denoted by *fd* (an open file descriptor such as one produced by `os.open()`).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.tcsetpgrp(*fd*, *pg*, */*)

Assign the process group tied to the terminal denoted by *fd* (an open file descriptor such as one produced by `os.open()`) to *pg*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.ttyname(*fd*, */*)

Give back a string naming the terminal device tied to file descriptor *fd*. Should *fd* not be tied to a terminal device, an exception is raised.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.unlockpt(*fd*, */*)

Unlock the slave pseudo-terminal device tied to the master pseudo-terminal device that file descriptor *fd* points at. The file descriptor *fd* stays open if the call fails.

Invokes the C standard library function `unlockpt()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](os-sendfile-to-os-set-blocking.md) · [Continue](os-write-to-os-writev.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
