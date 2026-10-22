# os: `os.utime()`

os.utime(*path*, *times=None*, ***, [*ns*, ]*dir_fd=None*, *follow_symlinks=True*)

Set the access and modified times of the file named by *path*.

`utime()` takes two optional parameters, *times* and *ns*. These declare the times set on *path* and are used like so:

- When *ns* is given, it has to be a 2-tuple shaped as `(atime_ns, mtime_ns)`, each member of which is an int that expresses nanoseconds.

- When *times* is not `None`, it has to be a 2-tuple shaped as `(atime, mtime)`, each member of which is an int or float that expresses seconds.

- When *times* is `None` and *ns* is left unspecified, this matches naming `ns=(atime_ns, mtime_ns)` where both times are the current time.

Naming tuples for both *times* and *ns* is an error.

Note that the precise times you set here may not come back from a later `stat()` call, depending on the resolution at which your operating system records access and modification times; consult `stat()`. The surest way to preserve exact times is to take the *st_atime_ns* and *st_mtime_ns* fields from the `os.stat()` result object and pass them through the *ns* parameter to `utime()`.

Support exists here for giving a file descriptor, for paths relative to directory descriptors, and for skipping symlink resolution.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.utime` with arguments `path`, `times`, `ns`, `dir_fd`.

Changed in version 3.3: Added the ability to give *path* as an open file descriptor, plus the *dir_fd*, *follow_symlinks*, and *ns* parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-symlink-to-os-unlink.md) · [Continue](os-walk.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
