# mmap.mmap: `find()`, `flush()`, `madvise()`, `move()`, `read()`, `read_byte()`, `readline()`, `resize()`, `rfind()`, `seek()`, `seekable()`, `size()`, `tell()`

closed

`True` if the file is closed.

Added in version 3.2.

 find(*sub*[, *start*[, *end*]])

Gives back the smallest index in the object at which the subsequence *sub* appears, with *sub* lying inside the range [*start*, *end*]. The optional *start* and *end* arguments follow slice-notation conventions. On failure it returns `-1`.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

 flush()

 flush(*offset*, *size*, */*)

Writes edits made to the file's in-memory copy back out to disk. Skipping this call leaves no assurance that the edits land on disk before the object goes away. When *offset* and *size* are given, only edits within that byte range get flushed; otherwise the entire span of the mapping is flushed. The *offset* must be a multiple of either `PAGESIZE` or `ALLOCATIONGRANULARITY`.

Success is signalled by returning `None`. A failed call raises an exception.

Changed in version 3.8: Formerly, under Windows a nonzero result meant success while zero meant error; under Unix a zero result meant success while an exception flagged an error.

 madvise(*option*[, *start*[, *length*]])

Pass the advice *option* along to the kernel regarding the memory region that starts at *start* and runs for *length* bytes. The *option* has to be one of the MADV_* constants the system provides. Omitting *start* and *length* makes the advice cover the whole mapping. On certain systems (Linux among them), *start* has to be a multiple of `PAGESIZE`.

Availability: Systems with the `madvise()` system call.

Added in version 3.8.

 move(*dest*, *src*, *count*)

Duplicate the *count* bytes that begin at offset *src*, placing them at the destination index *dest*. Should the mmap have been built with `ACCESS_READ`, any call to move raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

 read([*n*])

Hand back a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) of up to *n* bytes beginning at the current file position. When the argument is left off, `None`, or negative, return every byte from the current file position through the end of the mapping. The file position then advances to just past the bytes that were handed back.

Changed in version 3.3: Argument can be omitted or `None`.

 read_byte()

Hands back the byte at the current file position as an integer and moves the file position ahead by 1.

 readline()

Hands back one line, beginning at the current file position and running up to the following newline. The file position then advances to just past the bytes that were handed back.

 resize(*newsize*)

Resizes the map and the underlying file, if any.

Calling resize on a map made with an *access* of `ACCESS_READ` or `ACCESS_COPY` will raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception. Calling resize on a map made with *trackfd* equal to `False` will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception.

**On Windows**: An [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised by a resize when additional maps exist against the same named file. Resizing an anonymous map (that is, one against the pagefile) quietly builds a new map, copying the original data over up to the new size's length.

Changed in version 3.11: Now properly fails on a resize attempt while another map remains held; permits resizing an anonymous map under Windows

 rfind(*sub*[, *start*[, *end*]])

Gives back the largest index in the object at which the subsequence *sub* appears, with *sub* lying inside the range [*start*, *end*]. The optional *start* and *end* arguments follow slice-notation conventions. On failure it returns `-1`.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now accepted.

 seek(*pos*[, *whence*])

Set the file's current position. The *whence* argument is optional and defaults to `os.SEEK_SET` or `0` (absolute file positioning); the other options are `os.SEEK_CUR` or `1` (positioning relative to the current spot) and `os.SEEK_END` or `2` (positioning relative to the file's end).

Changed in version 3.13: Return the new absolute position instead of `None`.

 seekable()

Report whether the file allows seeking; this return value is always `True`.

Added in version 3.13.

 size()

Give back the file's length, which may exceed the size of the memory-mapped region.

 tell()

Hands back the file pointer's current position.

[Subject index](INDEX.md) · [Previous](mmap-mmap-class-to-mmap-mmap-close.md) · [Continue](mmap-mmap-write-to-mmap-mmap-write-byte.md) · [Owning module, declaration or section: mmap](mmap-mmap-class.md) · [Owning module, declaration or section: mmap.mmap](mmap-mmap-class-to-mmap-mmap-close.md)
