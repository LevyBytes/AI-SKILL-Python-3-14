# os: `os.fchmod()`, `os.fchown()`, `os.fdatasync()`, `os.fpathconf()`, `os.fstat()`, `os.fstatvfs()`, `os.fsync()`, `os.ftruncate()`

os.fchmod(*fd*, *mode*)

Switch the file named by *fd* over to the numeric *mode*. The `chmod()` docs cover the possible *mode* values. From Python 3.3 onward, this matches `os.chmod(fd, mode)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chmod` carrying arguments `path`, `mode`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

Changed in version 3.13: Windows support was added.

 os.fchown(*fd*, *uid*, *gid*)

Switch the owner and group id of the file named by *fd* to the numeric *uid* and *gid*. To leave either id alone, set it to -1. See `chown()`. From Python 3.3 onward, this matches `os.chown(fd, uid, gid)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chown` carrying arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for more information.

 os.fdatasync(*fd*)

Force the file with file descriptor *fd* to be written to disk. Does not force the metadata to be updated.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Note

This function is not available on MacOS.

 os.fpathconf(*fd*, *name*, */*)

Give back system configuration information that pertains to an open file. *name* picks out the configuration value to fetch; it may be a string that names a defined system value; you'll find such names spread over several standards (POSIX.1, Unix 95, Unix 98, plus more). A few platforms tack on extra names of their own. The names the host operating system knows are listed in the `pathconf_names` dictionary. For configuration variables absent from that mapping, an integer *name* is accepted as well.

When *name* is an unknown string, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. When a specific *name* value isn't supported by the host system, even though it appears in `pathconf_names`, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised carrying [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL) as the error number.

From Python 3.3 onward, this matches `os.pathconf(fd, name)`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.fstat(*fd*)

Fetch the status of file descriptor *fd*. Give back a `stat_result` object.

From Python 3.3 onward, this matches `os.stat(fd)`.

See also

The `stat()` function.

 os.fstatvfs(*fd*, */*)

Give back information about the filesystem holding the file tied to file descriptor *fd*, the way `statvfs()` does. From Python 3.3 onward, this matches `os.statvfs(fd)`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.fsync(*fd*)

Force the file carrying file descriptor *fd* out to disk. On Unix, the native `fsync()` function gets called; on Windows, the MS `_commit()` function does.

Should you be starting from a buffered Python [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *f*, do `f.flush()` first, and then `os.fsync(f.fileno())`, so that every internal buffer tied to *f* lands on disk.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

 os.ftruncate(*fd*, *length*, */*)

Truncate the file that file descriptor *fd* refers to, so its size is at most *length* bytes. From Python 3.3 onward, this matches `os.truncate(fd, length)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.truncate` carrying arguments `fd`, `length`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

Changed in version 3.5: Added support for Windows

[Subject index](INDEX.md) · [Previous](os-close-to-os-dup2.md) · [Continue](os-get-blocking-to-os-login-tty.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: File Descriptor Operations](os-close-to-os-dup2.md)
