# os: `os.link()`, `os.listdir()`, `os.listdrives()`, `os.listmounts()`, `os.listvolumes()`

os.link(*src*, *dst*, ***, *src_dir_fd=None*, *dst_dir_fd=None*, *follow_symlinks=True*)

Create a hard link named *dst* that points at *src*.

This function can support supplying *src_dir_fd* and/or *dst_dir_fd* to give paths relative to directory descriptors, and not following symlinks. On Windows the default value of *follow_symlinks* is `False`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.link` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.2: Added Windows support.

Changed in version 3.3: Added the *src_dir_fd*, *dst_dir_fd*, and *follow_symlinks* parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *src* and *dst*.

 os.listdir(*path='.'*)

Give back a list holding the names of the entries inside the directory named by *path*. The list comes back in arbitrary order and leaves out the special entries `'.'` and `'..'` even when they appear in the directory. Should a file be removed from or added to the directory while this function runs, whether a name for that file appears is unspecified.

*path* may be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). When *path* is of type `bytes` (whether directly or through the `PathLike` interface), the filenames returned come back as type `bytes` too; under all other conditions, they come back as type `str`.

This function can also support specifying a file descriptor; that file descriptor has to reference a directory.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.listdir` with argument `path`.

Note

To turn `str` filenames into `bytes`, use `fsencode()`.

See also

The `scandir()` function gives back directory entries together with file attribute information, delivering better performance for many common use cases.

Changed in version 3.2: The *path* parameter became optional.

Changed in version 3.3: Giving *path* as an open file descriptor is now supported.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.listdrives()

Give back a list holding the names of drives on a Windows system.

A drive name usually appears as `'C:\\'`. Not every drive name corresponds to a volume, and some may be unreachable for various reasons, among them permissions, network connectivity or missing media. This function performs no access test.

May raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when an error arises while gathering the drive names.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.listdrives` with no arguments.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Added in version 3.12.

 os.listmounts(*volume*)

Give back a list holding the mount points for a volume on a Windows system.

*volume* has to be expressed as a GUID path, of the kind returned by `os.listvolumes()`. Volumes may be mounted in several places or nowhere at all. In the latter case, the list comes back empty. Mount points not tied to a volume are not returned by this function.

The mount points this function returns are absolute paths, and may run longer than the drive name.

Raises [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when the volume is unrecognized or when an error arises while gathering the paths.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.listmounts` with argument `volume`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Added in version 3.12.

 os.listvolumes()

Give back a list holding the volumes on the system.

Volumes are usually expressed as a GUID path resembling `\\?\Volume{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\`. Files can generally be reached through a GUID path, permissions allowing. Users, however, are mostly unfamiliar with them, and so the suggested use of this function is to obtain mount points with `os.listmounts()`.

May raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when an error arises while gathering the volumes.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.listvolumes` with no arguments.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](os-chown-to-os-lchown.md) · [Continue](os-lstat-to-os-mkfifo.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
