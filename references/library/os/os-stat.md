# os: `os.stat()`

os.stat(*path*, ***, *dir_fd=None*, *follow_symlinks=True*)

Obtain the status of a file or a file descriptor. Perform what amounts to a `stat()` system call against the supplied path. *path* may arrive as either a string or bytes — whether directly or through the `PathLike` interface — or as an open file descriptor. Give back a `stat_result` object.

By default symlinks are followed by this function; to stat a symlink either add the argument `follow_symlinks=False` or use `lstat()`.

Support exists here for giving a file descriptor and for skipping symlink resolution.

On Windows, passing `follow_symlinks=False` turns off following all name-surrogate reparse points, which covers symlinks and directory junctions. Reparse points of other kinds that do not resemble links or that the operating system cannot follow are opened directly. While following a chain of multiple links, this may end with the original link being returned in place of the non-link that stopped full traversal. To get stat results for the final path in that situation, use the [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) function to resolve the path name as far as it can go and call `lstat()` on the result. None of this applies to dangling symlinks or junction points, which raise the usual exceptions.

Example:

```python
>>> import os
>>> statinfo = os.stat('somefile.txt')
>>> statinfo
os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026,
st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295,
st_mtime=1297230027, st_ctime=1297230027)
>>> statinfo.st_size
264

```

See also

`fstat()` and `lstat()` functions.

Changed in version 3.3: Added the *dir_fd* and *follow_symlinks* parameters, allowing a file descriptor in place of a path.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.8: On Windows, every reparse point the operating system can resolve is now followed, and passing `follow_symlinks=False` turns off following all name surrogate reparse points. Should the operating system arrive at a reparse point it cannot follow, *stat* now gives back the information for the original path as though `follow_symlinks=False` had been given instead of raising an error.

[Subject index](INDEX.md) · [Previous](os-direntry-stat.md) · [Continue](os-stat-result-class.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
