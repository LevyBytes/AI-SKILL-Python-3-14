# mmap / Memory-mapped file support: `mmap.mmap`, `close()`

*class *mmap.mmap(*fileno*, *length*, *flags=MAP_SHARED*, *prot=PROT_WRITE | PROT_READ*, *access=ACCESS_DEFAULT*, *offset=0*, ***, *trackfd=True*)

**(Unix version)** Maps *length* bytes taken from the file the descriptor *fileno* refers to and gives back a mmap object. With *length* set to `0`, the map's maximum length equals the file's size at the moment `mmap` is invoked.

The character of the mapping is set by *flags*. `MAP_PRIVATE` makes a private copy-on-write mapping, so any edits to the mmap object's contents stay local to this process, whereas `MAP_SHARED` builds a mapping shared with every other process that maps the same regions of the file. `MAP_SHARED` is the default. Certain systems offer extra flags, with the complete set documented under MAP_* constants.

When provided, *prot* states the memory protection you want; the pair of most useful values are `PROT_READ` and `PROT_WRITE`, declaring that the pages may be read or written. The *prot* default is `PROT_READ | PROT_WRITE`.

As an optional keyword argument, *access* can replace *flags* and *prot*. Supplying *flags*, *prot*, and *access* all at once is an error. Refer to the *access* description above to learn how this parameter works.

A non-negative integer may be given for *offset*. References through mmap are measured relative to that offset from the file's start. The default *offset* is 0. The value of *offset* has to be a multiple of `ALLOCATIONGRANULARITY`, which on Unix systems equals `PAGESIZE`.

When *trackfd* is `False`, the descriptor named by *fileno* is not duplicated, and the resulting `mmap` object carries no link to the map's backing file. Consequently the `size()` and `resize()` methods will not work. Such a mode helps cap how many file descriptors stay open.

On macOS, to keep the new memory mapping valid, the file behind the descriptor *fileno* is internally and automatically kept in sync with the physical backing store.

Changed in version 3.13: The *trackfd* parameter was added.

This example shows a simple way of using `mmap`:

```python
import mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(mm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints b"Hello  world!\n"
    # close the map
    mm.close()

```

`mmap` can also be used as a context manager in a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement:

```python
import mmap

with mmap.mmap(-1, 13) as mm:
    mm.write(b"Hello world!")

```

Added in version 3.2: Context manager support.

The example below shows how to set up an anonymous map and pass data between a parent process and its child:

```python
import mmap
import os

mm = mmap.mmap(-1, 13)
mm.write(b"Hello world!")

pid = os.fork()

if pid == 0:  # In a child process
    mm.seek(0)
    print(mm.readline())

    mm.close()

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.

Memory-mapped file objects support the following methods:

 close()

Closes the mmap. Any later calls to the object's other methods will trigger a ValueError exception. The open file itself stays open.

[Subject index](INDEX.md) · [Previous](mmap-mmap-class.md) · [Continue](mmap-mmap-find-to-mmap-mmap-tell.md) · [Owning module, declaration or section: mmap](mmap-mmap-class.md)
