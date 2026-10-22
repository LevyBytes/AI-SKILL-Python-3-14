# os: File descriptor creation and open flags

os.open(*path*, *flags*, *mode=0o777*, ***, *dir_fd=None*)

Open the file at *path*, applying assorted flags per *flags* and perhaps its mode per *mode*. As *mode* is computed, the current umask value is first masked out. Give back the file descriptor that belongs to the file just opened. That fresh file descriptor is non-inheritable.

For an account of the flag and mode values, consult the C run-time documentation; flag constants (like `O_RDONLY` and `O_WRONLY`) live in the `os` module. Notably, on Windows you need to add `O_BINARY` to open files in binary mode.

This function can handle paths relative to directory descriptors through the *dir_fd* parameter.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` carrying arguments `path`, `mode`, `flags`.

Changed in version 3.4: From here on the fresh file descriptor is non-inheritable.

Note

This function is meant for low-level I/O. For everyday use, reach for the built-in function `open()`, which gives back a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) carrying [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) and [`write()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.write) methods. To wrap a file descriptor in a file object, use `fdopen()`.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.5: Should the system call be interrupted while the signal handler raises no exception, the function nowadays retries that system call rather than raising an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

The constants below serve as options for the *flags* parameter to the `open()` function. You can combine them through the bitwise OR operator `|`. A few are unavailable on certain platforms. To read up on where each is available and how to use it, turn to the *[open(2)](https://manpages.debian.org/open(2))* manual page on Unix or to [the MSDN](https://msdn.microsoft.com/en-us/library/z0kc8e3z.aspx) on Windows.

 os.O_RDONLY

 os.O_WRONLY

 os.O_RDWR

 os.O_APPEND

 os.O_CREAT

 os.O_EXCL

 os.O_TRUNC

The above constants are available on Unix and Windows.

 os.O_DSYNC

 os.O_RSYNC

 os.O_SYNC

 os.O_NDELAY

 os.O_NONBLOCK

 os.O_NOCTTY

 os.O_CLOEXEC

The above constants are only available on Unix.

Changed in version 3.3: Add `O_CLOEXEC` constant.

 os.O_BINARY

 os.O_NOINHERIT

 os.O_SHORT_LIVED

 os.O_TEMPORARY

 os.O_RANDOM

 os.O_SEQUENTIAL

 os.O_TEXT

The above constants are only available on Windows.

[Subject index](INDEX.md) · [Previous](os-lseek-to-os-seek-data.md) · [Continue](os-o-evtonly-to-os-pipe.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
