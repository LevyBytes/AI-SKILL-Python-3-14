# tarfile: `TarFile.extractfile()`, `TarFile.extraction_filter`, `TarFile.add()`, `TarFile.addfile()`

TarFile.extractfile(*member*)

Pull a member out of the archive as a file object. The *member* argument may be a filename or a `TarInfo` object. When *member* is a regular file or a link, an [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) object comes back. For every other existing member, [`None`](https://docs.python.org/3.14/library/constants.html#None) comes back. Should *member* not be present in the archive, [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

Changed in version 3.3: Return an [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) object.

Changed in version 3.13: On the returned [`io.BufferedReader`](https://docs.python.org/3.14/library/io.html#io.BufferedReader) object, the `mode` attribute now always holds `'rb'`.

 TarFile.errorlevel*: [int](https://docs.python.org/3.14/library/functions.html#int)*

With *errorlevel* at `0`, errors stay silent during `TarFile.extract()` and `TarFile.extractall()`. They still show up as error messages in the debug output once *debug* climbs above 0. At `1` (the default), each *fatal* error gets raised as either an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) or a `FilterError` exception. At `2`, the *non-fatal* errors get raised as `TarError` exceptions in addition.

Certain exceptions — say, those from incorrect argument types or corrupted data — are raised no matter what.

Your own extraction filters ought to raise `FilterError` for the *fatal* cases and `ExtractError` for the *non-fatal* ones.

Keep in mind that once an exception fires, extraction may be only partial, and tidying up afterward falls to the user.

 TarFile.extraction_filter

Added in version 3.12.

The extraction filter that serves as the default for the *filter* argument on `extract()` and `extractall()`.

This attribute holds either `None` or a callable. Unlike the *filter* argument passed to `extract()`, it does not accept string names.

While `extraction_filter` stays `None` (its default), the extraction methods rely on the `data` filter.

You can assign this attribute on instances or override it in subclasses. Assigning it directly on the `TarFile` class to fix a global default works too; since that reaches every use of *tarfile*, though, the sound approach is to confine it to top-level applications or [`site configuration`](https://docs.python.org/3.14/library/site.html#module-site). For a global default set this way, wrap the filter function in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) to keep a `self` argument from being injected.

Changed in version 3.14: The default filter becomes `data`, which bars certain risky behaviors, among them links pointing at absolute paths or at paths beyond the destination. Earlier the default matched `fully_trusted`.

 TarFile.add(*name*, *arcname=None*, *recursive=True*, ***, *filter=None*)

Add the file *name* to the archive. The *name* may be any sort of file (directory, fifo, symbolic link, etc.). Where given, *arcname* supplies an alternate name for the file within the archive. Directories go in recursively by default, a behavior you can switch off by setting *recursive* to [`False`](https://docs.python.org/3.14/library/constants.html#False). Recursion adds entries in sorted order. Where *filter* is given, it should be a function taking a `TarInfo` object argument and returning the adjusted `TarInfo` object. If it returns [`None`](https://docs.python.org/3.14/library/constants.html#None) instead, that `TarInfo` object is omitted from the archive. See Examples for an example.

Changed in version 3.2: Added the *filter* parameter.

Changed in version 3.7: Recursion adds entries in sorted order.

 TarFile.addfile(*tarinfo*, *fileobj=None*)

[Subject index](INDEX.md) · [Previous](tarfile-getmember-to-tarfile-extract.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Owning module, declaration or section: tarfile.TarFile](tarfile-tarfile-class.md) · [Owning module, declaration or section: TarFile Objects](tarfile-tarfile-class.md) · [Required continuation of the source contract](tarfile-gettarinfo-to-tarfile-close.md)
