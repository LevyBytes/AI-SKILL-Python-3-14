# shutil: `shutil.copyfileobj()`, `shutil.copyfile()`, `shutil.SpecialFileError`, `shutil.SameFileError`, `shutil.copymode()`, `shutil.copystat()`

### Directory and files operations

 shutil.copyfileobj(*fsrc*, *fdst*[, *length*])

Transfer the contents of the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-object) *fsrc* into the file-like object *fdst*. When supplied, the integer *length* sets the buffer size. Specifically, passing a negative *length* tells the function to move the data without iterating over the source in chunks; the default behavior reads the data in chunks so that memory consumption stays bounded. Keep in mind that when *fsrc* has a current file position other than 0, only the portion from that position through the end of the file gets copied.

`copyfileobj()` makes *no* promise that the destination stream is flushed once the copy finishes. Should you need to read from the destination after the copy completes (say, to inspect a temporary file copied from a HTTP stream), be sure you have invoked [`flush()`](https://docs.python.org/3.14/library/io.html#io.IOBase.flush) or [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) on the file-like object before you try reading the destination file.

 shutil.copyfile(*src*, *dst*, ***, *follow_symlinks=True*)

In the most efficient way available, copy the contents (no metadata) of the file called *src* to a file called *dst*, returning *dst*. Both *src* and *dst* are [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) or path names supplied as strings.

The value *dst* has to be the full target file name; consult `copy()` for a variant that takes a destination directory path. Should *src* and *dst* refer to the same file, `SameFileError` is raised.

A writable destination is required; if not, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception gets raised. An existing *dst* will be overwritten. This function cannot copy special files like character or block devices and pipes.

When *follow_symlinks* is false and *src* is a symbolic link, the function creates a fresh symbolic link rather than copying the file that *src* points at.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.

Changed in version 3.3: Formerly an [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) was thrown rather than an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). The *follow_symlinks* argument was introduced, and *dst* is now the return value.

Changed in version 3.4: `SameFileError` is now raised in place of `Error`. Because `SameFileError` derives from `Error`, the switch remains backward compatible.

Changed in version 3.8: To copy a file with greater efficiency, the routine may internally call fast-copy syscalls that are specific to the platform. Refer to the Platform-dependent efficient copy operations section.

 *exception *shutil.SpecialFileError

This exception gets raised when `copyfile()` or `copytree()` try to copy a named pipe.

Added in version 2.7.

 *exception *shutil.SameFileError

This exception gets raised when source and destination in `copyfile()` point to the same file.

Added in version 3.4.

 shutil.copymode(*src*, *dst*, ***, *follow_symlinks=True*)

Transfer the permission bits from *src* over to *dst*. The contents, owner, and group of the file stay untouched. Both *src* and *dst* are [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) or path names supplied as strings. With *follow_symlinks* set to false, and *src* and *dst* both being symbolic links, `copymode()` tries to alter the mode of *dst* itself (in place of the file it targets). Not every platform offers this capability; refer to `copystat()` for further detail. When `copymode()` is unable to alter symbolic links on the local platform yet is asked to, it takes no action and returns.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copymode` with arguments `src`, `dst`.

Changed in version 3.3: The *follow_symlinks* argument was introduced.

 shutil.copystat(*src*, *dst*, ***, *follow_symlinks=True*)

From *src* to *dst*, transfer these items: the flags, the last modification time, the last access time, and the permission bits. Under Linux, `copystat()` additionally copies the "extended attributes" wherever feasible. The contents, owner, and group of the file stay untouched. Both *src* and *dst* are [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) or path names supplied as strings.

With *follow_symlinks* set to false, and both *src* and *dst* referring to symbolic links, `copystat()` acts on the symbolic links themselves instead of the files those links point at — pulling the information from the *src* symbolic link and writing it onto the *dst* symbolic link.

Note

Examining and modifying symbolic links is not something every platform supports. Python itself can report which features are available locally.

- If `os.chmod in os.supports_follow_symlinks` is `True`, the permission bits of a symbolic link can be altered by `copystat()`.

- If `os.utime in os.supports_follow_symlinks` is `True`, then the symbolic link's access and modification timestamps can be revised by `copystat()`.

- If `os.chflags in os.supports_follow_symlinks` is `True`, the flags on a symbolic link can be revised by `copystat()`. (`os.chflags` is not available on all platforms.)

On platforms where part or all of this capability is missing, `copystat()` copies whatever it can when told to modify a symbolic link. `copystat()` never reports failure.

Please see [`os.supports_follow_symlinks`](https://docs.python.org/3.14/library/os.html#os.supports_follow_symlinks) for more information.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copystat` with arguments `src`, `dst`.

Changed in version 3.3: The *follow_symlinks* argument was introduced, together with handling for Linux extended attributes.

[Subject index](INDEX.md) · [Previous](shutil-high-level-file-operations.md) · [Continue](shutil-copy-to-shutil-copytree.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
