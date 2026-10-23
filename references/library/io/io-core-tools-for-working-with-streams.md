# io`io` - Core tools for working with streams

### `io` - Core tools for working with streams

**Source code:** [Lib/io.py](https://github.com/python/cpython/tree/3.14/Lib/io.py)

---

### Overview

Python's primary machinery for handling assorted forms of I/O lives in the `io` module. I/O comes in three principal flavors: *text I/O*, *binary I/O* and *raw I/O*. Each is a broad category, and a range of backing stores may sit behind any of them. When a concrete object falls into one of these categories, it is referred to as a [file object](https://docs.python.org/3.14/glossary.html#term-file-object). You will also hear it called a *stream* or *file-like object*.

Whatever category it belongs to, every concrete stream object carries a set of abilities as well: it may be read-only, write-only, or both readable and writable. Some support unrestricted random access, letting you seek forward or backward to any position, while others permit only sequential access — a socket or pipe, for instance.

Streams are strict about the kind of data they accept. Handing a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object to a binary stream's `write()` method, for example, will trigger a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). The same happens if you pass a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object to the `write()` method on a text stream.

Changed in version 3.3: Calls that formerly raised [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) now raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), given that `IOError` is now an alias of `OSError`.

[Subject index](INDEX.md) · [Continue](text-i-o.md)
