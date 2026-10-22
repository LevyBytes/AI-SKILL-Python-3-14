# tarfile: `tarfile.TarInfo`

### TarInfo Objects

A `TarInfo` object stands for a single member within a `TarFile`. Beyond holding every mandatory attribute of a file (file type, size, time, permissions, owner, and so on), it offers a handful of handy methods for figuring out its type. It does *not* hold the file's data itself.

`TarInfo` objects are returned by `TarFile`'s methods `getmember()`, `getmembers()` and `gettarinfo()`.

If you alter the objects handed back by `getmember()` or `getmembers()`, every later operation on the archive is affected. When that side effect is not what you want, either reach for [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#module-copy) or invoke the `replace()` method, which produces an altered copy in a single step.

A number of attributes may be assigned `None` to signal that some metadata is either unknown or not in use. The various `TarInfo` methods treat `None` in their own ways:

- The matching metadata is disregarded by the `extract()` and `extractall()` methods, which leave it at a default value.

- `addfile()` will fail.

- `list()` will print a placeholder string.

 *class *tarfile.TarInfo(*name=''*)

Create a `TarInfo` object.

[Subject index](INDEX.md) · [Previous](tarfile-gettarinfo-to-tarfile-close.md) · [Continue](tarinfo-tobuf.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
