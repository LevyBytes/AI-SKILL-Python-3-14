# os: `os.lstat()`, `os.mkdir()`, `os.makedirs()`, `os.mkfifo()`

os.lstat(*path*, ***, *dir_fd=None*)

Carry out the equivalent of an `lstat()` system call on the given path. Resembles `stat()`, but does not follow symbolic links. Give back a `stat_result` object.

On platforms lacking symbolic link support, this acts as an alias for `stat()`.

Since Python 3.3, this matches `os.stat(path, dir_fd=dir_fd, follow_symlinks=False)`.

This function can also support paths relative to directory descriptors.

See also

The `stat()` function.

Changed in version 3.2: Symbolic links on Windows 6.0 (Vista) gained support.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: On Windows, now opens reparse points that stand for another path (name surrogates), among them symbolic links and directory junctions. Reparse points of other kinds are resolved by the operating system the same way as for `stat()`.

 os.mkdir(*path*, *mode=0o777*, ***, *dir_fd=None*)

Create a directory named *path* with numeric mode *mode*.

Should the directory already exist, [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised. Should a parent directory in the path be missing, [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is raised.

On some systems, *mode* is disregarded. Where it is honored, the current umask value is masked out first. Should bits beyond the last 9 (that is, beyond the last 3 digits of the octal representation of the *mode*) be set, their meaning is platform-dependent. On certain platforms they are disregarded and you should call `chmod()` explicitly to apply them.

On Windows, a *mode* of `0o700` is treated specially to apply access control to the new directory so that only the current user and administrators have access. All other values of *mode* are disregarded.

This function can also support paths relative to directory descriptors.

You can also create temporary directories; consult the [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile) module's [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp) function.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.mkdir` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: Windows now handles a *mode* of `0o700`.

 os.makedirs(*name*, *mode=0o777*, *exist_ok=False*)

Recursive directory creation function. Resembles `mkdir()`, but builds every intermediate-level directory required to contain the leaf directory.

The *mode* parameter is handed to `mkdir()` for building the leaf directory; consult the mkdir() description for how it gets interpreted. To set the file permission bits of any freshly created parent directories you can set the umask ahead of invoking `makedirs()`. The file permission bits of parent directories that already exist are not changed.

Should *exist_ok* be `False` (the default), a [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised when the target directory already exists.

Note

`makedirs()` gets confused when the path elements to create include `pardir` (e.g. ".." on UNIX systems).

This function handles UNC paths correctly.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.mkdir` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.2: Added the *exist_ok* parameter.

Changed in version 3.4.1: Before Python 3.4.1, with *exist_ok* set to `True` for an already-present directory, `makedirs()` would nonetheless raise an error whenever *mode* differed from the mode on the directory that already existed. As that behavior had no safe implementation, Python 3.4.1 removed it. Consult [bpo-21082](https://bugs.python.org/issue?@action=redirect&bpo=21082).

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: For freshly created intermediate-level directories, the file permission bits are no longer influenced by the *mode* argument.

 os.mkfifo(*path*, *mode=0o666*, ***, *dir_fd=None*)

Build a FIFO (a named pipe) called *path* whose numeric mode is *mode*. The current umask value gets masked out of the mode beforehand.

This function can also support paths relative to directory descriptors.

FIFOs are pipes you can access just like regular files. A FIFO stays around until it is deleted (for instance via `os.unlink()`). Typically a FIFO acts as a meeting point linking processes of the "client" and "server" kind: reading is opened on the FIFO by the server while writing is opened on it by the client. Keep in mind that `mkfifo()` does not open the FIFO — all it does is create that meeting point.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-link-to-os-listvolumes.md) · [Continue](os-mknod-to-os-readlink.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
