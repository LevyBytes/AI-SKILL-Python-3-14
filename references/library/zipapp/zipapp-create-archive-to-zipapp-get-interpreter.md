# zipapp - Python API

### Python API

Two convenience functions are defined by the module:

`zipapp.create_archive(*source*, *target=None*, *interpreter=None*, *main=None*, *filter=None*, *compressed=False*)`

Build an application archive out of *source*. That source may be any one of these:

- A directory’s name, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) pointing at a directory — whereupon a brand-new application archive is assembled from that directory’s contents.

- The name of an application archive file that already exists, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) pointing at such a file — whereupon the file is copied over to the target (adjusted to reflect whatever was passed for the *interpreter* argument). Include the `.pyz` extension in the name where it’s called for.

- A file object opened for reading in bytes mode. What it holds should be an application archive, and the file object is taken to sit at the archive’s start.

Where the archive ends up depends on the *target* argument:

- Give a file name, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object), and the archive lands in that file.

- Give an open file object and the archive is written into it; that object has to be open for writing in bytes mode.

- Drop the target altogether (or pass `None`) and the source has to be a directory; the target then becomes a file bearing the source’s name with `.pyz` appended.

By the *interpreter* argument you name the Python interpreter the archive will run under. It’s laid down as a “shebang” line at the archive’s head. The OS reads it on POSIX, while on Windows the Python launcher takes care of it. Leave *interpreter* out and no shebang line gets written. Supply an interpreter together with a target that is a filename, and the target file’s executable bit gets switched on.

By the *main* argument you name the callable to serve as the archive’s main program. It’s permitted only when the source is a directory that doesn’t already carry a `__main__.py` file. The *main* argument is expected to read “pkg.module:callable”, and the archive runs by importing “pkg.module” and calling that callable with no arguments. Omitting *main* is an error if the source is a directory lacking a `__main__.py` file, since otherwise the archive that results wouldn’t be executable.

The optional *filter* argument names a callback handed a Path object that stands for the path of the file under consideration (taken relative to the source directory). It ought to return `True` when that file should go in.

The optional *compressed* argument decides whether files get compressed. Set it to `True` and the archive’s files are squeezed with the deflate method; leave it and the files sit there uncompressed. The argument is inert while an existing archive is being copied.

When a file object is handed in for *source* or *target*, closing it after the create_archive call is the caller’s job.

While copying an existing archive, file objects you provide need only `read` and `readline`, or `write`, methods. While building an archive from a directory, a target that is a file object gets handed to the `zipfile.ZipFile` class and must furnish whatever methods that class requires.

Changed in version 3.7: Added the *filter* and *compressed* parameters.

`zipapp.get_interpreter(*archive*)`

Give back the interpreter named in the `#!` line at the archive’s start. Absent a `#!` line, return [`None`](https://docs.python.org/3.14/library/constants.html#None). The *archive* argument may be a filename or a file-like object opened for reading in bytes mode. It’s presumed to be positioned at the archive’s start.

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Continue](examples.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)
