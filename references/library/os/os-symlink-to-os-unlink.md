# os: `os.symlink()`, `os.sync()`, `os.truncate()`, `os.unlink()`

os.symlink(*src*, *dst*, *target_is_directory=False*, ***, *dir_fd=None*)

Create a symbolic link named *dst* that points at *src*.

The *src* parameter denotes what the link aims at (the file or directory it links to), while *dst* gives the name for the link that gets created.

On Windows, a symlink stands for either a file or a directory, and does not change to match the target on the fly. When the target is present, the symlink type gets created to match it. Otherwise, the symlink gets created as a directory when *target_is_directory* is `True` or as a file symlink (the default) otherwise. On non-Windows platforms, *target_is_directory* is disregarded.

This function can support paths relative to directory descriptors.

Note

On newer releases of Windows 10, unprivileged accounts can create symlinks once Developer Mode is enabled. When Developer Mode is unavailable or disabled, the *SeCreateSymbolicLinkPrivilege* privilege is required, or the process has to run as an administrator.

[`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised when the function gets called by an unprivileged user.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.symlink` with arguments `src`, `dst`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

This function is restricted on WASI; consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

Changed in version 3.2: Symbolic links on Windows 6.0 (Vista) gained support.

Changed in version 3.3: Added the *dir_fd* parameter, and now permit *target_is_directory* on non-Windows platforms.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *src* and *dst*.

Changed in version 3.8: Unelevated symlinks on Windows with Developer Mode gained support.

 os.sync()

Force every pending write out to disk.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

 os.truncate(*path*, *length*)

Truncate the file matching *path*, so that it is no larger than *length* bytes in size.

This function can support specifying a file descriptor.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.truncate` with arguments `path`, `length`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Added in version 3.3.

Changed in version 3.5: Added support for Windows

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.unlink(*path*, ***, *dir_fd=None*)

Remove (delete) the file *path*. This function behaves semantically just like `remove()`; the `unlink` name is its traditional Unix name. Please consult the documentation for `remove()` for further information.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-statvfs-to-os-supports-follow-symlinks.md) · [Continue](os-utime.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
