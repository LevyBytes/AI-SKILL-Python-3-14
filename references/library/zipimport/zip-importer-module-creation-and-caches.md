# zipimport.zipimporter: `create_module()`, `exec_module()`, `find_spec()`, `get_code()`, `get_data()`, `get_filename()`, `get_source()`, `is_package()`, `load_module()`, `invalidate_caches()`

create_module(*spec*)

A realization of [`importlib.abc.Loader.create_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.create_module) that hands back [`None`](https://docs.python.org/3.14/library/constants.html#None) so the default behavior is explicitly requested.

Added in version 3.10.

 exec_module(*module*)

A realization of [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module).

Added in version 3.10.

 find_spec(*fullname*, *target=None*)

A realization of [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec).

Added in version 3.10.

 get_code(*fullname*)

Hands back the code object belonging to the named module. Throws `ZipImportError` when that module could not be imported.

 get_data(*pathname*)

Hands back the data tied to *pathname*. Throws [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when the file is missing.

Changed in version 3.3: Where [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) was once thrown, that name now stands as an alias for [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 get_filename(*fullname*)

Hands back whatever `__file__` would hold had the named module been imported. Throws `ZipImportError` when the module could not be imported.

Added in version 3.1.

 get_source(*fullname*)

Hands back the source text for the named module. Throws `ZipImportError` when the module is absent, and yields [`None`](https://docs.python.org/3.14/library/constants.html#None) when the archive carries the module yet keeps no source for it.

 is_package(*fullname*)

Yields `True` when the module named by *fullname* turns out to be a package. Throws `ZipImportError` when that module cannot be located.

 load_module(*fullname*)

Brings in the module named by *fullname*. The *fullname* has to be the complete dotted module name. On success the imported module comes back; on failure `ZipImportError` is thrown.

Deprecated since version 3.10, slated for removal in 3.15: turn to `exec_module()` in its place.

 invalidate_caches()

Empties the internal cache holding details about the files discovered inside the ZIP archive.

Added in version 3.10.

 archive

The name of the ZIP file the importer is bound to, minus any subpath.

 prefix

The location inside the ZIP file under which modules get searched. For zipimporter objects aimed at the ZIP file's root this is an empty string.

Joined together with a slash, the `archive` and `prefix` attributes reproduce the original *archivepath* argument handed to the `zipimporter` constructor.

[Subject index](INDEX.md) · [Previous](zipimport-zipimporter-class.md) · [Continue](examples.md) · [Owning module, declaration or section: zipimport](zipimport-zipimporterror.md) · [Owning module, declaration or section: zipimport.zipimporter](zipimport-zipimporter-class.md) · [Owning module, declaration or section: zipimporter Objects](zipimport-zipimporter-class.md)
