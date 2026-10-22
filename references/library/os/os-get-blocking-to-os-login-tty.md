# os: `os.get_blocking()`, `os.grantpt()`, `os.isatty()`, `os.lockf()`, `os.F_LOCK`, `os.F_TLOCK`, `os.F_ULOCK`, `os.F_TEST`, `os.login_tty()`

os.get_blocking(*fd*, */*)

Fetch the blocking mode of the file descriptor: `False` when the `O_NONBLOCK` flag is set, `True` when the flag is cleared.

See also `set_blocking()` and [`socket.socket.setblocking()`](https://docs.python.org/3.14/library/socket.html#socket.socket.setblocking).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

On Windows, this function is limited to pipes.

Added in version 3.5.

Changed in version 3.12: Added support for pipes on Windows.

 os.grantpt(*fd*, */*)

Grant access to the slave pseudo-terminal device paired with the master pseudo-terminal device that file descriptor *fd* refers to. The file descriptor *fd* is left open on failure.

Calls the C standard library function `grantpt()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.13.

 os.isatty(*fd*, */*)

Give back `True` when file descriptor *fd* is open and tied to a tty(-like) device, otherwise `False`.

 os.lockf(*fd*, *cmd*, *len*, */*)

Set, test, or release a POSIX lock over an open file descriptor. *fd* is one such open file descriptor. *cmd* picks the command to apply - one of `F_LOCK`, `F_TLOCK`, `F_ULOCK` or `F_TEST`. *len* picks the stretch of the file to lock.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.lockf` with arguments `fd`, `cmd`, `len`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.F_LOCK

 os.F_TLOCK

 os.F_ULOCK

 os.F_TEST

Flags that specify what action `lockf()` will take.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.login_tty(*fd*, */*)

Ready the tty for which fd is a file descriptor so it can host a fresh login session. Make the calling process a session leader; promote the tty to controlling tty and also to the calling process's stdin, stdout, and stderr; close fd.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](os-fchmod-to-os-ftruncate.md) · [Continue](os-lseek-to-os-seek-data.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
