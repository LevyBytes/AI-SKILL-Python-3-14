# os: `os.replace()`, `os.rmdir()`, `os.scandir()`, `scandir.close()`

os.replace(*src*, *dst*, ***, *src_dir_fd=None*, *dst_dir_fd=None*)

Rename the file or directory *src* to *dst*. Should *dst* be a non-empty directory, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Should *dst* exist and be a file, it gets replaced quietly provided the user holds permission. The operation may fail when *src* and *dst* sit on different filesystems. On success, the renaming is an atomic operation (a POSIX requirement).

This function can support supplying *src_dir_fd* and/or *dst_dir_fd* to give paths relative to directory descriptors.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Added in version 3.3.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *src* and *dst*.

 os.rmdir(*path*, ***, *dir_fd=None*)

Remove (delete) the directory *path*. Should the directory be missing or be non-empty, a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) or an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised respectively. To remove entire directory trees, [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) can serve.

This function can support paths relative to directory descriptors.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.rmdir` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.scandir(*path='.'*)

Give back an iterator over `os.DirEntry` objects that match the entries inside the directory *path* names. In arbitrary order the entries get yielded, while the special entries `'.'` and `'..'` stay excluded. Should a file get removed from or added to the directory after the iterator was built, whether an entry for that file appears is unspecified.

Reaching for `scandir()` rather than `listdir()` can sharply boost the performance of code that also wants file type or file attribute information, because `os.DirEntry` objects surface this information whenever the operating system supplies it during a directory scan. Every `os.DirEntry` method may issue a system call, yet `is_dir()` and `is_file()` generally need a system call only for symbolic links; `os.DirEntry.stat()` always needs a system call on Unix but needs one only for symbolic links on Windows.

*path* may be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). When *path* is of type `bytes` (whether directly or through the `PathLike` interface), the type of the `name` and `path` attributes on each `os.DirEntry` is `bytes`; under all other conditions, they are of type `str`.

This function can also support specifying a file descriptor; that file descriptor has to reference a directory.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.scandir` with argument `path`.

The `scandir()` iterator honors the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol and offers the following method:

 scandir.close()

Close the iterator and let go of acquired resources.

This runs automatically once the iterator is exhausted or garbage collected, or once an error occurs while iterating. Even so, calling it explicitly or using the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement is advisable.

Added in version 3.6.

The example below demonstrates a simple use of `scandir()` to list all the files (directories excluded) inside the given *path* that don't begin with `'.'`. The `entry.is_file()` call generally will not trigger an extra system call:

```python
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

```

Note

On Unix-based systems, `scandir()` draws on the system's [opendir()](https://pubs.opengroup.org/onlinepubs/009695399/functions/opendir.html) and [readdir()](https://pubs.opengroup.org/onlinepubs/009695399/functions/readdir_r.html) functions. On Windows, it draws on the Win32 [FindFirstFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418(v=vs.85).aspx) and [FindNextFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428(v=vs.85).aspx) functions.

Added in version 3.5.

Changed in version 3.6: Gained support for the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol along with the `close()` method. A `scandir()` iterator that is neither exhausted nor closed explicitly will, in its destructor, emit a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning).

The function accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: Added support for file descriptors on Unix.

[Subject index](INDEX.md) · [Previous](os-remove-to-os-renames.md) · [Continue](os-direntry-class-to-os-direntry-is-junction.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
