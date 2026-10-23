# errno`errno` - Standard errno system symbols

# Errno

### `errno` - Standard errno system symbols

---

Standard `errno` system symbols are exposed through this module. Each symbol carries an integer value matching the corresponding code. Names and descriptions are taken from `linux/include/errno.h`, which ought to cover everything.

 errno.errorcode

A dictionary that maps each errno value back to its string name on the host system. As an example, `errno.errorcode[errno.EPERM]` resolves to `'EPERM'`.

For turning a numeric code into a readable message, call [`os.strerror()`](https://docs.python.org/3.14/library/os.html#os.strerror).

Within the list that follows, any symbol unused on your current platform stays undefined by the module. You can read the exact set of defined symbols from `errno.errorcode.keys()`. The symbols that may appear include:

 errno.EPERM

Operation not permitted. The exception this maps to is [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError).

 errno.ENOENT

No such file or directory. The exception this maps to is [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError).

 errno.ESRCH

No such process. The exception this maps to is [`ProcessLookupError`](https://docs.python.org/3.14/library/exceptions.html#ProcessLookupError).

 errno.EINTR

Interrupted system call. The exception this maps to is [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError).

 errno.EIO

I/O error

 errno.ENXIO

No such device or address

 errno.E2BIG

Arg list too long

 errno.ENOEXEC

Exec format error

 errno.EBADF

Bad file number

 errno.ECHILD

No child processes. The exception this maps to is [`ChildProcessError`](https://docs.python.org/3.14/library/exceptions.html#ChildProcessError).

 errno.EAGAIN

Try again. The exception this maps to is [`BlockingIOError`](https://docs.python.org/3.14/library/exceptions.html#BlockingIOError).

 errno.ENOMEM

Out of memory

 errno.EACCES

Permission denied. The exception this maps to is [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError).

 errno.EFAULT

Bad address

 errno.ENOTBLK

Block device required

 errno.EBUSY

Device or resource busy

[Subject index](INDEX.md) · [Continue](errno-eexist-to-errno-enolck.md)
