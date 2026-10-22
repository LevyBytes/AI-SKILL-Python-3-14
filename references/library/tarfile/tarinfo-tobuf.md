# tarfile: `TarInfo.frombuf()`, `TarInfo.fromtarfile()`, `TarInfo.tobuf()`

*classmethod *TarInfo.frombuf(*buf*, *encoding*, *errors*)

Build and hand back a `TarInfo` object from the string buffer *buf*.

Raises `HeaderError` if the buffer is invalid.

 *classmethod *TarInfo.fromtarfile(*tarfile*)

Read the next member out of the `TarFile` object *tarfile* and give it back as a `TarInfo` object.

 TarInfo.tobuf(*format=DEFAULT_FORMAT*, *encoding=ENCODING*, *errors='surrogateescape'*)

Produce a string buffer from a `TarInfo` object. The constructor of the `TarFile` class documents what the arguments mean.

Changed in version 3.2: The *errors* argument now defaults to `'surrogateescape'`.

A `TarInfo` object has the following public data attributes:

 TarInfo.name*: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*

Name of the archive member.

 TarInfo.size*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Size in bytes.

 TarInfo.mtime*: [int](https://docs.python.org/3.14/library/functions.html#int) | [float](https://docs.python.org/3.14/library/functions.html#float)*

Time of last modification expressed in seconds since the [epoch](https://docs.python.org/3.14/library/time.html#epoch), matching [`os.stat_result.st_mtime`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_mtime).

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

 TarInfo.mode*: [int](https://docs.python.org/3.14/library/functions.html#int)*

Permission bits, as for [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod).

Changed in version 3.12: May be assigned `None`, in which case `extract()` and `extractall()` will not apply this attribute during extraction.

[Subject index](INDEX.md) · [Previous](tarfile-tarinfo-class.md) · [Continue](tarinfo-type-to-tarinfo-isfile.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Owning module, declaration or section: tarfile.TarInfo](tarfile-tarinfo-class.md) · [Owning module, declaration or section: TarInfo Objects](tarfile-tarinfo-class.md)
