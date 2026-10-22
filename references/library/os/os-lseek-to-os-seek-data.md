# os: `os.lseek()`, `os.SEEK_SET`, `os.SEEK_CUR`, `os.SEEK_END`, `os.SEEK_HOLE`, `os.SEEK_DATA`

os.lseek(*fd*, *pos*, *whence*, */*)

Move the current position of file descriptor *fd* to position *pos*, adjusted by *whence*, and give back the new position in bytes measured from the start of the file. The valid *whence* values are:

- `SEEK_SET` or `0` – set *pos* relative to the beginning of the file

- `SEEK_CUR` or `1` – set *pos* relative to the current file position

- `SEEK_END` or `2` – set *pos* relative to the end of the file

- `SEEK_HOLE` – set *pos* to the next data location, relative to *pos*

- `SEEK_DATA` – set *pos* to the next data hole, relative to *pos*

Changed in version 3.3: Add support for `SEEK_HOLE` and `SEEK_DATA`.

 os.SEEK_SET

 os.SEEK_CUR

 os.SEEK_END

Arguments for the `lseek()` function as well as the [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek) method on [file-like objects](https://docs.python.org/3.14/glossary.html#term-file-object), supplying the whence by which the file position indicator gets adjusted.

`SEEK_SET`

Adjust the file position relative to the beginning of the file.

`SEEK_CUR`

Adjust the file position relative to the current file position.

`SEEK_END`

Adjust the file position relative to the end of the file.

Their values are 0, 1, and 2, respectively.

 os.SEEK_HOLE

 os.SEEK_DATA

Arguments for the `lseek()` function as well as the [`seek()`](https://docs.python.org/3.14/library/io.html#io.IOBase.seek) method on [file-like objects](https://docs.python.org/3.14/glossary.html#term-file-object), used to seek file data and holes within sparsely allocated files.

`SEEK_DATA`

Shift the file offset, measured from the seek position, to the next spot that holds data.

`SEEK_HOLE`

Shift the file offset, measured from the seek position, to the next spot that holds a hole. A hole means a run of zeros.

Note

These operations only make sense for filesystems that support them.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.1, macOS, Unix

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](os-get-blocking-to-os-login-tty.md) · [Continue](os-open-to-os-o-text.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
