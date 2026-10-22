# shutil: `shutil.register_archive_format()`, `shutil.unregister_archive_format()`, `shutil.unpack_archive()`, `shutil.register_unpack_format()`, `shutil.unregister_unpack_format()`

`shutil.register_archive_format(*name*, *function*[, *extra_args*[, *description*]])`

Sign up an archiver under the format *name*.

*function* is the callable tasked with building archives. It’s handed the *base_name* of the file to make, followed by the *base_dir* (defaulting to [`os.curdir`](https://docs.python.org/3.14/library/os.html#os.curdir)) where archiving begins. Anything further arrives as keyword arguments: *owner*, *group*, *dry_run*, and *logger* (just as passed to `make_archive()`).

When *function* carries the custom attribute `function.supports_root_dir` set to `True`, the *root_dir* argument rides along as a keyword argument. Otherwise the process’s working directory is briefly pointed at *root_dir* before *function* is called, and in that case `make_archive()` forfeits thread safety.

When provided, *extra_args* is a sequence of `(name, value)` pairs fed in as additional keyword arguments whenever the archiver callable runs.

*description* feeds `get_archive_formats()`, which hands back the archiver list. It defaults to an empty string.

Changed in version 3.12: Added support for functions supporting the *root_dir* argument.

`shutil.unregister_archive_format(*name*)`

Drop the archive format *name* from the roster of supported formats.

`shutil.unpack_archive(*filename*[, *extract_dir*[, *format*[, *filter*]]])`

Unpack an archive. *filename* gives the archive’s full path.

*extract_dir* names the destination directory the archive expands into. Leave it out and the current working directory serves.

*format* selects how the archive is laid out. Valid choices are “zip”, “tar”, “gztar”, “bztar”, “xztar”, and “zstdtar” — plus whatever else you’ve registered through `register_unpack_format()`. Omit it and `unpack_archive()` reads the archive’s file-name extension and looks for an unpacker registered against that extension. When none turns up, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

The keyword-only *filter* argument flows through to the underlying unpacking function. For zip files, *filter* isn’t taken. For tar files, going with `'data'` is advised (the default as of Python 3.14) unless you’re relying on features peculiar to tar and UNIX-like filesystems. (Particulars live in [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter).)

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.unpack_archive` with the arguments `filename`, `extract_dir`, `format`.

Warning

Don’t ever unpack archives from sources you don’t trust without looking them over first. Files can end up created beyond the path named in the *extract_dir* argument — think members whose filenames are absolute or contain “..” components.

Starting with Python 3.14, the out-of-the-box settings for each built-in format (zip plus tar files) fend off the gravest of these security pitfalls, though they won’t catch *every* unintended behavior. For tar-specific guidance, read the [Hints for further verification](https://docs.python.org/3.14/library/tarfile.html#tarfile-further-verification) section.

Changed in version 3.7: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *filename* and *extract_dir*.

Changed in version 3.12: Added the *filter* argument.

`shutil.register_unpack_format(*name*, *extensions*, *function*[, *extra_args*[, *description*]])`

Sign up an unpack format. *name* is the format’s name and *extensions* is a list of the extensions tied to it, such as `.zip` for Zip files.

*function* is the callable charged with unpacking archives. It’s handed:

- as a positional argument, the archive’s path;

- as a positional argument, the directory into which the archive must be unpacked;

- perhaps a *filter* keyword argument, when one was supplied to `unpack_archive()`;

- further keyword arguments, laid out by *extra_args* as a sequence of `(name, value)` tuples.

You may pass *description* to characterize the format; the `get_unpack_formats()` function then returns it.

`shutil.unregister_unpack_format(*name*)`

Remove an unpack format from the registry. *name* is the format’s name.

[Subject index](INDEX.md) · [Previous](shutil-make-archive-to-shutil-get-archive-formats.md) · [Continue](shutil-get-unpack-formats.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Owning module, declaration or section: Archiving operations](shutil-make-archive-to-shutil-get-archive-formats.md)
