# fcntl: `fcntl.fcntl()`, `fcntl.ioctl()`

## fcntl - The fcntl and ioctl system calls

### `fcntl` - The `fcntl` and `ioctl` system calls

---

File and I/O control over file descriptors is what this module handles. It wraps the Unix `fcntl()` and `ioctl()` routines. Consult the *[fcntl(2)](https://manpages.debian.org/fcntl(2))* and *[ioctl(2)](https://manpages.debian.org/ioctl(2))* Unix manual pages to get the complete picture.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Every function here expects a file descriptor *fd* as its initial argument. That may be an integer file descriptor — for instance, the one `sys.stdin.fileno()` hands back — or an [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) object such as `sys.stdin` on its own, which offers a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) returning an actual file descriptor.

Changed in version 3.3: Where this module's operations once raised an [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError), they raise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) today.

Changed in version 3.8: For sealing [`os.memfd_create()`](https://docs.python.org/3.14/library/os.html#os.memfd_create) file descriptors, the `fcntl` module now carries the `F_ADD_SEALS`, `F_GET_SEALS`, and `F_SEAL_*` constants.

Changed in version 3.9: Under macOS, the `fcntl` module surfaces the `F_GETPATH` constant, which recovers a file's path given a file descriptor. Under Linux(>=3.15), the `fcntl` module surfaces the `F_OFD_GETLK`, `F_OFD_SETLK` and `F_OFD_SETLKW` constants, applied when dealing with open file description locks.

Changed in version 3.10: Under Linux >= 2.6.11, the `fcntl` module surfaces the `F_GETPIPE_SZ` and `F_SETPIPE_SZ` constants, which respectively let you inspect and adjust a pipe’s size.

Changed in version 3.11: Under FreeBSD, the `fcntl` module surfaces the `F_DUP2FD` and `F_DUP2FD_CLOEXEC` constants for duplicating a file descriptor, with the latter additionally setting the `FD_CLOEXEC` flag.

Changed in version 3.12: Under Linux >= 4.5, the `fcntl` module surfaces the `FICLONE` and `FICLONERANGE` constants, letting one file share part of its data with another through reflinking on certain filesystems (for example btrfs, OCFS2, and XFS). The usual name for this behavior is “copy-on-write”.

Changed in version 3.13: Under Linux >= 2.6.32, the `fcntl` module surfaces the `F_GETOWN_EX`, `F_SETOWN_EX`, `F_OWNER_TID`, `F_OWNER_PID`, `F_OWNER_PGRP` constants for routing I/O availability signals toward a particular thread, process, or process group. Under Linux >= 4.13, the `fcntl` module offers the `F_GET_RW_HINT`, `F_SET_RW_HINT`, `F_GET_FILE_RW_HINT`, `F_SET_FILE_RW_HINT`, and `RWH_WRITE_LIFE_*` constants, which tell the kernel about the relative anticipated lifetime of writes on a given inode or through a particular open file description. Across Linux >= 5.1 and NetBSD, the `fcntl` module provides the `F_SEAL_FUTURE_WRITE` constant intended for the `F_ADD_SEALS` and `F_GET_SEALS` operations. Under FreeBSD, the `fcntl` module brings out the `F_READAHEAD`, `F_ISUNIONSTACK`, and `F_KINFO` constants. Across macOS and FreeBSD, the `fcntl` module makes the `F_RDAHEAD` constant available. Across NetBSD and AIX, the `fcntl` module yields the `F_CLOSEM` constant. Under NetBSD alone, the `fcntl` module surfaces the `F_MAXFD` constant. Across macOS and NetBSD, the `fcntl` module yields the `F_GETNOSIGPIPE` and `F_SETNOSIGPIPE` constant.

Changed in version 3.14: Under Linux >= 6.1, the `fcntl` module surfaces the `F_DUPFD_QUERY`, used to query a file descriptor that points at the same file.

The module defines the following functions:

 fcntl.fcntl(*fd*, *cmd*, *arg=0*, */*)

Carry out the operation *cmd* against file descriptor *fd* (file objects that supply a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method work too). Which values you give for *cmd* depend on the operating system, and they appear as constants within the `fcntl` module, bearing the same names found in the corresponding C header files. The *arg* argument may be an integer value, a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), or a string. Both the type and size of *arg* have to line up with the type and size that the operation's argument calls for, per the corresponding C documentation.

Where *arg* is an integer, what comes back is the integer return value from the C `fcntl()` call.

Where the argument is a bytes-like object, it stands for a binary structure — say, one produced via [`struct.pack()`](https://docs.python.org/3.14/library/struct.html#struct.pack). String values get encoded into binary through UTF-8 encoding. That binary data is copied into a buffer, and the buffer's address is handed to the C `fcntl()` call. Following a successful call, the return value is the buffer's contents recast as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. Whatever comes back matches the *arg* argument in length. A cap of 1024 bytes applies here.

Should the `fcntl()` call fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Note

Where the type or size of *arg* fails to match the type or size that the operation's argument expects (say, passing an integer where a pointer belongs, or where the operating system writes back more than 1024 bytes into the buffer), the usual outcome is a segmentation violation or some more insidious data corruption.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `fcntl.fcntl` with arguments `fd`, `cmd`, `arg`.

Changed in version 3.14: Arbitrary [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) are now supported, rather than [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) alone.

 fcntl.ioctl(*fd*, *request*, *arg=0*, *mutate_flag=True*, */*)

Apart from argument handling that grows still more involved, this function behaves just like the `fcntl()` function.

The *request* parameter has to fit within 32-bits or 64-bits, contingent on the platform. You can locate further constants worth using as the *request* argument in the [`termios`](https://docs.python.org/3.14/library/termios.html#module-termios) module, carrying the same names found in the corresponding C header files.

The parameter *arg* can be an integer, a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), or a string. Both the type and size of *arg* have to line up with the type and size that the operation's argument calls for, per the corresponding C documentation.

When *arg* offers no read-write buffer interface, or when *mutate_flag* is false, the behavior matches the `fcntl()` function.

When *arg* does provide the read-write buffer interface (such as [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray)) and *mutate_flag* is true (its default), then the buffer is, in effect, fed to the underlying `ioctl()` system call; that call's return code is relayed back to the calling Python, and the buffer's revised contents capture the effect of the `ioctl()`. That description simplifies matters somewhat, since a supplied buffer shorter than 1024 bytes is first copied into a static buffer of 1024 bytes, which then goes to `ioctl()` and is copied back into the supplied buffer.

Should the `ioctl()` call fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Note

Where the type or size of *arg* fails to match the type or size of the operation’s argument (say, passing an integer where a pointer belongs, or where the operating system writes back more than 1024 bytes into the buffer, or where the mutable bytes-like object's size is too small), the usual outcome is a segmentation violation or some more insidious data corruption.

An example:

```python
>>> import array, fcntl, struct, termios, os
>>> os.getpgrp()
13341
>>> struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))[0]
13341
>>> buf = array.array('h', [0])
>>> fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
0
>>> buf
array('h', [13341])

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `fcntl.ioctl` with arguments `fd`, `request`, `arg`.

Changed in version 3.14: The GIL gets released for the duration of every system call. Any system call that fails with EINTR is retried on its own.

[Subject index](INDEX.md) · [Continue](fcntl-flock-to-fcntl-lock-nb.md)
