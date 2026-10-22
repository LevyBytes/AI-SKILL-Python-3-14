# Built-in Functions — Contract: The example below puts the dir_fd parameter of the `os.open()` function to use, opening a file relative to a given directory:

The example below puts the [dir_fd](https://docs.python.org/3.14/library/os.html#dir-fd) parameter of the [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) function to use, opening a file relative to a given directory:

```python
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor

```

Which kind of [file object](https://docs.python.org/3.14/glossary.html#term-file-object) the `open()` function returns is governed by the mode. When `open()` opens a file in a text mode (`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), it hands back a subclass of [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) (to be precise [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper)). Whenever a binary mode with buffering is used to open a file, what comes back is a subclass of [`io.BufferedIOBase`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase). The precise class differs: in read binary mode, it hands back an [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader); in write binary and append binary modes, it hands back an [`io.BufferedWriter`](https://docs.python.org/3.14/library/io.html#io.BufferedWriter), and in read/write mode, it hands back an [`io.BufferedRandom`](https://docs.python.org/3.14/library/io.html#io.BufferedRandom). When buffering is turned off, the raw stream, a subclass of [`io.RawIOBase`](https://docs.python.org/3.14/library/io.html#io.RawIOBase), [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO), comes back.

See also the file handling modules, such as [`fileinput`](https://docs.python.org/3.14/library/fileinput.html#module-fileinput), [`io`](https://docs.python.org/3.14/library/io.html#module-io) (where `open()` is declared), [`os`](https://docs.python.org/3.14/library/os.html#module-os), [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path), [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile), and [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `open` with arguments `path`, `mode`, `flags`.

The original call may have had its `mode` and `flags` arguments altered or deduced from it.

Changed in version 3.3:

- The *opener* parameter was added.

- The `'x'` mode was added.

- [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) used to be raised, it is now an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

- [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) now gets raised whenever a file already present is opened in exclusive creation mode (`'x'`).

Changed in version 3.4:

- The file is now non-inheritable.

Changed in version 3.5:

- Should the system call get interrupted while the signal handler raises no exception, the function now reattempts that system call rather than raising an [`InterruptedError`](https://docs.python.org/3.14/library/exceptions.html#InterruptedError) exception (consult [**PEP 475**](https://peps.python.org/pep-0475/) for the reasoning).

- The `'namereplace'` error handler was added.

Changed in version 3.6:

- Support added to accept objects implementing [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike).

- Under Windows, when a console buffer is opened the result may be some subclass of [`io.RawIOBase`](https://docs.python.org/3.14/library/io.html#io.RawIOBase) apart from [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO).

Changed in version 3.11: The `'U'` mode has been removed.

[Subject index](INDEX.md) · [Previous](open.md) · [Continue](INDEX.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md) · [Owning module, declaration or section: open](open.md)
