# mmap: `mmap.mmap`

## mmap - Memory-mapped file support

### `mmap` - Memory-mapped file support

---

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further details.

Objects representing memory-mapped files act as a hybrid of [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [file objects](https://docs.python.org/3.14/glossary.html#term-file-object). An mmap object can stand in for a `bytearray` almost anywhere one is expected; for instance, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module can scan across a memory-mapped file. Writing a lone byte is done with `obj[index] = 97`, while a slice assignment like `obj[i1:i2] = b'...'` replaces a subsequence. Reading and writing relative to the present file position is supported too, and `seek()` lets you move that position around within the file.

The `mmap` constructor builds a memory-mapped file, and its signature varies between Unix and Windows. On both platforms a file descriptor referring to a file opened for update must be supplied. To map a file object that already exists in Python, call its [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method to fetch the proper *fileno* value. Alternatively, opening the file via [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) hands back a file descriptor straight away (and that file still has to be closed afterward).

Note

When you plan to memory-map a buffered file that is writable, call [`flush()`](https://docs.python.org/3.14/library/io.html#io.IOBase.flush) on it beforehand. Doing so guarantees that buffer-level changes made locally actually reach the mapping.

On both the Unix and Windows forms of the constructor, *access* is available as an optional keyword argument. Four values are accepted for *access*: `ACCESS_READ`, `ACCESS_WRITE`, or `ACCESS_COPY` select read-only, write-through, or copy-on-write memory respectively, while `ACCESS_DEFAULT` defers to *prot*. Both Unix and Windows honor *access*. When *access* is left out, the Windows mmap yields a write-through mapping. Whatever the access type, the starting memory contents come from the file you named. Writing to an `ACCESS_READ` map triggers a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception. Writing to an `ACCESS_WRITE` map updates both memory and the file behind it. Writing to an `ACCESS_COPY` map updates memory only and leaves the backing file untouched.

Changed in version 3.7: Added `ACCESS_DEFAULT` constant.

For anonymous memory, pass -1 as the fileno together with the length.

 *class *mmap.mmap(*fileno*, *length*, *tagname=None*, *access=ACCESS_DEFAULT*, *offset=0*)

**(Windows version)** Maps *length* bytes drawn from the file identified by the handle *fileno* and produces a mmap object. Should *length* exceed the file's present size, the file grows to hold *length* bytes. When *length* is `0`, the map's maximum length matches the file's current size — but an empty file makes Windows raise an exception, since no empty mapping can exist on Windows.

If *tagname* is supplied and not `None`, it is a string serving as a tag name for the mapping. On Windows you may keep numerous distinct mappings against one file. Naming an already-existing tag opens that tag; otherwise a fresh tag bearing this name comes into being. Leaving the parameter out, or passing `None`, produces an unnamed mapping. Steering clear of the *tagname* parameter helps keep your code portable across Unix and Windows.

A non-negative integer may be given for *offset*. References through mmap are measured relative to that offset from the file's start. The default *offset* is 0. The value of *offset* has to be a multiple of `ALLOCATIONGRANULARITY`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `mmap.__new__` with arguments `fileno`, `length`, `access`, `offset`.

[Subject index](INDEX.md) · [Continue](mmap-mmap-class-to-mmap-mmap-close.md)
