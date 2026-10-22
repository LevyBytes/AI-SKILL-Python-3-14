# os: `os.PathLike`

*class *os.PathLike

An [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) for objects standing for a file system path, e.g. [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath).

Added in version 3.6.

 *abstractmethod *__fspath__()

Return the file system path representation of the object.

This method should return only a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, with `str` being preferred.

[Subject index](INDEX.md) · [Previous](os-fsdecode-to-os-fspath.md) · [Continue](os-getenv-to-os-getpgrp.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Parameters](os-ctermid-to-os-fsencode.md)
