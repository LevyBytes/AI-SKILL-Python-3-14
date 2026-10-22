# os: `os.remove()`, `os.removedirs()`, `os.rename()`, `os.renames()`

When the *path* is a string object (whether directly or through a `PathLike` interface), the result comes back as a string object as well, and the call may raise a UnicodeDecodeError. When the *path* is a bytes object (direct or indirect), a bytes object is what comes back.

This function can also support paths relative to directory descriptors.

To resolve a path that might hold links, reach for [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath), which correctly handles recursion together with platform differences.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.2: Symbolic links on Windows 6.0 (Vista) gained support.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) on Unix.

Changed in version 3.8: On Windows, both a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) and a bytes object are accepted.

Added support for directory junctions, and changed so it returns the substitution path (which usually carries the `\\?\` prefix) in place of the optional "print name" field that used to be returned.

 os.remove(*path*, ***, *dir_fd=None*)

Remove (delete) the file *path*. Should *path* be a directory, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. Reach for `rmdir()` to remove directories. Should the file not exist, a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) is raised.

This function can support paths relative to directory descriptors.

On Windows, trying to remove a file that is currently in use triggers an exception; on Unix, the directory entry goes away but the storage held by the file is not reclaimed until the original file stops being in use.

This function behaves semantically just like `unlink()`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.removedirs(*name*)

Remove directories recursively. Operates like `rmdir()`, except that, once the leaf directory has been removed successfully, `removedirs()` works its way upward, attempting to remove each parent directory named in *path* until an error appears (which is then ignored, since it usually means a parent directory is not empty). For instance, `os.removedirs('foo/bar/baz')` first removes the directory `'foo/bar/baz'`, and then removes `'foo/bar'` and `'foo'` if they are empty. Raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when the leaf directory could not be removed successfully.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.rename(*src*, *dst*, ***, *src_dir_fd=None*, *dst_dir_fd=None*)

Rename the file or directory *src* to *dst*. Should *dst* exist, the operation fails with an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) subclass under a number of circumstances:

On Windows, when *dst* exists a [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is always raised. The operation may fail when *src* and *dst* sit on different filesystems. Reach for [`shutil.move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) to allow moves across a different filesystem.

On Unix, when *src* is a file and *dst* is a directory or the reverse, an [`IsADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#IsADirectoryError) or a [`NotADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#NotADirectoryError) is raised respectively. When both are directories and *dst* is empty, *dst* gets replaced quietly. When *dst* is a non-empty directory, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised. When both are files, *dst* gets replaced quietly provided the user holds permission. The operation may fail on certain Unix flavors when *src* and *dst* sit on different filesystems. On success, the renaming is an atomic operation (a POSIX requirement).

This function can support supplying *src_dir_fd* and/or *dst_dir_fd* to give paths relative to directory descriptors.

If cross-platform overwriting of the destination is what you want, reach for `replace()`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Changed in version 3.3: Added the *src_dir_fd* and *dst_dir_fd* parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *src* and *dst*.

 os.renames(*old*, *new*)

Recursive directory or file renaming function. Operates like `rename()`, except that creation of any intermediate directories needed to make the new pathname valid is attempted first. After the rename, directories matching the rightmost path segments of the old name get pruned away with `removedirs()`.

Note

This function can fail with the new directory structure already built when you lack the permissions required to remove the leaf directory or file.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *old* and *new*.

[Subject index](INDEX.md) · [Continue](os-replace-to-scandir-close.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Owning module, declaration or section: os.readlink](os-mknod-to-os-readlink.md) · [Preceding source contract and version conditions](os-mknod-to-os-readlink.md)
