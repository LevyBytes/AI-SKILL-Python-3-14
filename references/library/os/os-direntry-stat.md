# os.DirEntry: `stat()`

stat(***, *follow_symlinks=True*)

Give back a `stat_result` object for this entry. By default this method follows symbolic links; to stat a symbolic link add the `follow_symlinks=False` argument.

On Unix, a system call is always needed by this method. On Windows, a system call is needed only when *follow_symlinks* is `True` while the entry happens to be a reparse point (a symbolic link or a directory junction, say).

On Windows, zero is always the value of the `st_ino`, `st_dev` and `st_nlink` attributes on the `stat_result`. Call `os.stat()` to obtain these attributes.

The `os.DirEntry` object caches the result, keeping one cache for *follow_symlinks* `True` and another for `False`. Call `os.stat()` to retrieve current information.

Note that several attributes and methods of `os.DirEntry` line up nicely with those of [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path). In particular, the `name` attribute carries the same meaning, as do the `is_dir()`, `is_file()`, `is_symlink()`, `is_junction()`, and `stat()` methods.

Added in version 3.5.

Changed in version 3.6: The `PathLike` interface gained support. On Windows, [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) paths gained support too.

Changed in version 3.12: On Windows, a stat result's `st_ctime` attribute is deprecated. As the file creation time, `st_birthtime` is the proper source, and `st_ctime` may, in later releases, switch to returning zero or the metadata change time, if available.

[Subject index](INDEX.md) · [Previous](os-direntry-class-to-os-direntry-is-junction.md) · [Continue](os-stat.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: os.DirEntry](os-direntry-class-to-os-direntry-is-junction.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
