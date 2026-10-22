# os: `os.get_terminal_size()`

### Querying the size of a terminal

Added in version 3.3.

 os.get_terminal_size(*fd=STDOUT_FILENO*, */*)

Give back the size of the terminal window as `(columns, lines)`, a tuple of type `terminal_size`.

The optional argument `fd` (default `STDOUT_FILENO`, or standard output) selects which file descriptor gets queried.

When the file descriptor has no terminal attached, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

[`shutil.get_terminal_size()`](https://docs.python.org/3.14/library/shutil.html#shutil.get_terminal_size) is the high-level function meant for ordinary use, while `os.get_terminal_size` is the low-level implementation.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

[Subject index](INDEX.md) · [Previous](os-write-to-os-writev.md) · [Continue](os-terminal-size-class.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
