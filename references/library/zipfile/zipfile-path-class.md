# zipfile: `zipfile.Path`

*class *zipfile.Path

A class offering part of what [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) exposes, together with the complete [`importlib.resources.abc.Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable) interface.

Added in version 3.8.

### Path objects

 *class *zipfile.Path(*root*, *at=''*)

Build a Path object from a `root` zipfile (this can be a `ZipFile` instance or a `file` that the `ZipFile` constructor would accept).

The `at` argument pins down where this Path sits inside the zipfile — for example ‘dir/file.txt’, ‘dir/’, or ‘’. It defaults to the empty string, which points at the root.

Note

[Subject index](INDEX.md) · [Previous](zipfile-zipfile-class.md) · [Continue](zipfile-pyzipfile-class.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Previous](zipfile-read-to-zipfile-comment.md) · [Required continuation of the source contract](path-name-to-path-read-bytes.md)
