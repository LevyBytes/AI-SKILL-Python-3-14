# tarfile: `tarfile.TarFile`

*class *tarfile.TarFile

The class behind reading and writing tar archives. Rather than instantiating it directly, call `tarfile.open()`. See TarFile Objects.

### TarFile Objects

The `TarFile` object exposes an interface onto a tar archive. Such an archive is a sequence of blocks. Within it, an archive member (a stored file) consists of a header block trailed by data blocks. The same file may be stored more than once inside a single tar archive. A `TarInfo` object stands in for each archive member; consult TarInfo Objects for the details.

A `TarFile` object can serve as a context manager inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Once the block finishes, it closes on its own. Bear in mind that if an exception occurs, an archive opened for writing is left unfinalized; the only thing closed is the file object it uses internally. The Examples section presents a use case.

Added in version 3.2: Added support for the context management protocol.

 *class *tarfile.TarFile(*name=None*, *mode='r'*, *fileobj=None*, *format=DEFAULT_FORMAT*, *tarinfo=TarInfo*, *dereference=False*, *ignore_zeros=False*, *encoding=ENCODING*, *errors='surrogateescape'*, *pax_headers=None*, *debug=0*, *errorlevel=1*, *stream=False*)

Each of the arguments that follow is optional and is also reachable as an instance attribute.

The *name* argument is the pathname of the archive and may be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). You can leave it out when *fileobj* is supplied; the file object’s `name` attribute is then consulted if present.

The *mode* argument is one of `'r'` to read an existing archive, `'a'` to append data onto an existing file, `'w'` to make a fresh file that overwrites any existing one, or `'x'` to make a fresh file only when none already exists.

When *fileobj* is supplied, it serves for reading or writing data. Where it can be worked out, *fileobj*’s mode takes precedence over *mode*. Usage of *fileobj* begins at position 0.

Note

*fileobj* is not closed, when `TarFile` is closed.

The *format* argument governs the archive format on write. Its value has to be one of the module-level constants `USTAR_FORMAT`, `GNU_FORMAT` or `PAX_FORMAT`. On read, the format is detected automatically, even where a single archive mixes several formats.

You can supply the *tarinfo* argument to swap out the default `TarInfo` class for an alternative.

When *dereference* is [`False`](https://docs.python.org/3.14/library/constants.html#False), symbolic and hard links are added to the archive. When it is [`True`](https://docs.python.org/3.14/library/constants.html#True), the contents of the targeted files are added instead. On systems without symbolic link support this makes no difference.

When *ignore_zeros* is [`False`](https://docs.python.org/3.14/library/constants.html#False), an empty block is treated as the archive's end. When it is [`True`](https://docs.python.org/3.14/library/constants.html#True), empty (and invalid) blocks are skipped and the code tries to pull out as many members as it can. This helps only when reading concatenated or damaged archives.

The *debug* argument ranges from `0` (no debug messages) through `3` (all debug messages). Those messages go to `sys.stderr`.

The *errorlevel* argument dictates how extraction errors are dealt with, see `the corresponding attribute`.

Together the *encoding* and *errors* arguments set the character encoding used to read or write the archive and decide how conversion errors are treated. Most users will find the defaults sufficient. The Unicode issues section covers this thoroughly.

The *pax_headers* argument is an optional dictionary of strings that gets added as a pax global header whenever *format* is `PAX_FORMAT`.

When *stream* is [`True`](https://docs.python.org/3.14/library/constants.html#True), the archive's per-file info is not cached during reading, which conserves memory.

Changed in version 3.2: The *errors* argument now defaults to `'surrogateescape'`.

Changed in version 3.5: The `'x'` (exclusive creation) mode was added.

Changed in version 3.6: The *name* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: Add the *stream* parameter.

[Subject index](INDEX.md) · [Previous](tarfile-open.md) · [Continue](tarfile-is-tarfile-to-tarfile-lnktype.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Previous](tarfile-symtype-to-tarfile-default-format.md) · [Continue](tarfile-getmember-to-tarfile-extract.md)
