# os / Files and Directories: `os.DirEntry`, `inode()`, `is_dir()`, `is_file()`, `is_symlink()`, `is_junction()`

*class *os.DirEntry

Object yielded by `scandir()` to surface the file path and other file attributes of a directory entry.

`scandir()` supplies as much of this information as it can without issuing extra system calls. Whenever a `stat()` or `lstat()` system call is made, the `os.DirEntry` object caches the result.

`os.DirEntry` instances are not meant to be kept in long-lived data structures; when you know the file metadata has changed or when a long stretch of time has gone by since `scandir()` was called, call `os.stat(entry.path)` to retrieve current information.

Because the `os.DirEntry` methods can trigger operating system calls, they may also raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). When you need very fine-grained control over errors, you can catch `OSError` while calling one of the `os.DirEntry` methods and handle it as suits you.

So that it is directly usable as a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object), `os.DirEntry` implements the `PathLike` interface.

`DirEntry` objects are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the type of the path ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)).

The attributes and methods on an `os.DirEntry` instance are these:

 name

The entry's base filename, taken relative to the `scandir()` *path* argument.

The `name` attribute is `bytes` when the `scandir()` *path* argument is of type `bytes` and `str` otherwise. Reach for `fsdecode()` to decode byte filenames.

 path

The entry's full path name: equal to `os.path.join(scandir_path, entry.name)` where *scandir_path* is the `scandir()` *path* argument. The path is absolute only when the `scandir()` *path* argument was absolute. When the `scandir()` *path* argument was a file descriptor, the [`path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) attribute equals the `name` attribute.

The [`path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) attribute is `bytes` when the `scandir()` *path* argument is of type `bytes` and `str` otherwise. Reach for `fsdecode()` to decode byte filenames.

 inode()

Give back the inode number of the entry.

The result is cached on the `os.DirEntry` object. Reach for `os.stat(entry.path, follow_symlinks=False).st_ino` to retrieve current information.

On the first, uncached call, Windows needs a system call but Unix does not.

 is_dir(***, *follow_symlinks=True*)

Give back `True` when this entry is a directory or a symbolic link aiming at a directory; give back `False` when the entry is or aims at any other kind of file, or when it no longer exists.

When *follow_symlinks* is `False`, give back `True` only when this entry is a directory (without following symlinks); give back `False` when the entry is any other kind of file or when it no longer exists.

The `os.DirEntry` object caches the result, keeping one cache for *follow_symlinks* `True` and another for `False`. Call `os.stat()` together with [`stat.S_ISDIR()`](https://docs.python.org/3.14/library/stat.html#stat.S_ISDIR) to retrieve current information.

On that first, uncached call, most of the time no system call is required. To be precise, for non-symlinks, a system call is needed by neither Windows nor Unix, save for certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`. Where the entry is a symlink, following the symlink requires a system call unless *follow_symlinks* is `False`.

This method can raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), such as [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError), but [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is caught and not raised.

 is_file(***, *follow_symlinks=True*)

Give back `True` when this entry is a file or a symbolic link aiming at a file; give back `False` when the entry is or aims at a directory or other non-file entry, or when it no longer exists.

When *follow_symlinks* is `False`, give back `True` only when this entry is a file (without following symlinks); give back `False` when the entry is a directory or other non-file entry, or when it no longer exists.

The result is cached on the `os.DirEntry` object. Caching, the system calls made, and the exceptions raised follow `is_dir()`.

 is_symlink()

Give back `True` when this entry is a symbolic link (even a broken one); give back `False` when the entry aims at a directory or any kind of file, or when it no longer exists.

The result is cached on the `os.DirEntry` object. Call [`os.path.islink()`](https://docs.python.org/3.14/library/os.path.html#os.path.islink) to retrieve current information.

On that first, uncached call, most of the time no system call is required. To be precise, a system call is needed by neither Windows nor Unix, save for certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`.

This method can raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), such as [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError), but [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is caught and not raised.

 is_junction()

Give back `True` when this entry is a junction (even a broken one); give back `False` when the entry aims at a regular directory, any kind of file, a symlink, or when it no longer exists.

The result is cached on the `os.DirEntry` object. Call [`os.path.isjunction()`](https://docs.python.org/3.14/library/os.path.html#os.path.isjunction) to retrieve current information.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](os-replace-to-scandir-close.md) · [Continue](os-direntry-stat.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
