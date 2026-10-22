# os: `os.fsdecode()`, `os.fspath()`

os.fsdecode(*filename*)

Decode the [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) *filename* from the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler); return [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) unchanged.

`fsencode()` is the reverse function.

Added in version 3.2.

Changed in version 3.6: Now also accepts objects that implement the `os.PathLike` interface.

 os.fspath(*path*)

Return the file system representation of the path.

When a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) is passed in, it comes back unchanged. Otherwise `__fspath__()` gets called and its value is returned provided it is a `str` or `bytes` object. In every other case, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](os-ctermid-to-os-fsencode.md) · [Continue](os-pathlike-class.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)
