# mmap.mmap: `write()`, `write_byte()`

write(*bytes*)

Place the bytes from *bytes* into memory at the file pointer's current position and return how many bytes were written (never under `len(bytes)`, because a failed write raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError)). Afterward the file position moves to just beyond the freshly written bytes. Should the mmap have been built with `ACCESS_READ`, any attempt to write to it raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

Changed in version 3.6: The count of written bytes is now given back as the return value.

 write_byte(*byte*)

Place the integer *byte* into memory at the file pointer's current position; the file position moves ahead by `1`. Should the mmap have been built with `ACCESS_READ`, any attempt to write to it raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

[Subject index](INDEX.md) · [Previous](mmap-mmap-find-to-mmap-mmap-tell.md) · [Continue](mmap-madv-normal-to-mmap-madv-free-reuse.md) · [Owning module, declaration or section: mmap](mmap-mmap-class.md) · [Owning module, declaration or section: mmap.mmap](mmap-mmap-class-to-mmap-mmap-close.md)
