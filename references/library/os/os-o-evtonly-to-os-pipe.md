# os: `os.O_EVTONLY`, `os.O_FSYNC`, `os.O_SYMLINK`, `os.O_NOFOLLOW_ANY`, `os.O_ASYNC`, `os.O_DIRECT`, `os.O_DIRECTORY`, `os.O_NOFOLLOW`, `os.O_NOATIME`, `os.O_PATH`, `os.O_TMPFILE`, `os.O_SHLOCK`, `os.O_EXLOCK`, `os.openpty()`, `os.pipe()`

os.O_EVTONLY

 os.O_FSYNC

 os.O_SYMLINK

 os.O_NOFOLLOW_ANY

The above constants are only available on macOS.

Changed in version 3.10: Add `O_EVTONLY`, `O_FSYNC`, `O_SYMLINK` and `O_NOFOLLOW_ANY` constants.

 os.O_ASYNC

 os.O_DIRECT

 os.O_DIRECTORY

 os.O_NOFOLLOW

 os.O_NOATIME

 os.O_PATH

 os.O_TMPFILE

 os.O_SHLOCK

 os.O_EXLOCK

The constants above are extensions, absent whenever the C library leaves them undefined.

Changed in version 3.4: `O_PATH` was added on systems that support it. `O_TMPFILE` was added, available solely on Linux Kernel 3.11 or newer.

 os.openpty()

Open a fresh pseudo-terminal pair. Hand back two file descriptors `(master, slave)`, one for the pty and one for the tty in that order. Those fresh file descriptors are non-inheritable. When you want a (somewhat) more portable route, reach for the [`pty`](https://docs.python.org/3.14/library/pty.html#module-pty) module.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Changed in version 3.4: From here on the fresh file descriptors are non-inheritable.

 os.pipe()

[Subject index](INDEX.md) · [Previous](os-open-to-os-o-text.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md) · [Required continuation of the source contract](os-pipe2-to-os-preadv.md)
