# os: `os.write()`, `os.writev()`

os.write(*fd*, *str*, */*)

Write the bytestring contained in *str* to file descriptor *fd*.

The count of bytes actually written is returned.

Note

This routine targets low-level I/O and is meant for a file descriptor such as one produced by `os.open()` or `pipe()`. When you want to write a "file object" produced by the built-in function [`open()`](https://docs.python.org/3.14/library/functions.html#open), by `popen()`, or by `fdopen()`, or [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) or [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr), reach instead for its [`write()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.write) method.

Changed in version 3.5: When the system call is interrupted and the signal handler raises no exception, the routine now repeats the system call rather than raising an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

 os.writev(*fd*, *buffers*, */*)

Write the data held in *buffers* to file descriptor *fd*. *buffers* has to be a sequence of [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). The buffers get handled in array order. The first buffer is written out in full before the second is reached, and so forth.

The grand total of bytes actually written is returned.

A ceiling on how many buffers may be supplied can be imposed by the operating system (the `sysconf()` value `'SC_IOV_MAX'`).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](os-splice-to-os-unlockpt.md) · [Continue](os-get-terminal-size.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
