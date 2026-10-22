# os: `os.chown()`, `os.chroot()`, `os.fchdir()`, `os.getcwd()`, `os.getcwdb()`, `os.lchflags()`, `os.lchmod()`, `os.lchown()`

os.chown(*path*, *uid*, *gid*, ***, *dir_fd=None*, *follow_symlinks=True*)

Reassign the owning user and group of *path* to the numeric *uid* and *gid*. Leaving an id untouched is done by passing -1 for it.

Support is available here for giving a file descriptor, for paths relative to directory descriptors, and for skipping symlink resolution.

Consult [`shutil.chown()`](https://docs.python.org/3.14/library/shutil.html#shutil.chown) for a higher-level function that takes names as well as numeric ids.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

This function is restricted on WASI; consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

Changed in version 3.3: Added the ability to give *path* as an open file descriptor, along with the *dir_fd* and *follow_symlinks* arguments.

Changed in version 3.6: Supports a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.chroot(*path*)

Switch the root directory of the current process to *path*.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI, not Android.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.fchdir(*fd*)

Switch the current working directory to the directory denoted by the file descriptor *fd*. The descriptor has to reference an opened directory, not an open file. Since Python 3.3, this matches `os.chdir(fd)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chdir` with argument `path`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.getcwd()

Give back a string holding the current working directory.

 os.getcwdb()

Give back a bytestring holding the current working directory.

Changed in version 3.8: The function now relies on UTF-8 encoding on Windows in place of the ANSI code page: consult [**PEP 529**](https://peps.python.org/pep-0529/) for the reasoning. The function is no longer deprecated on Windows.

 os.lchflags(*path*, *flags*)

Assign the flags of *path* to the numeric *flags*, much like `chflags()`, except that symbolic links are not followed. Since Python 3.3, this matches `os.chflags(path, flags, follow_symlinks=False)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chflags` with arguments `path`, `flags`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.lchmod(*path*, *mode*)

Switch the mode of *path* to the numeric *mode*. When path is a symlink, this acts on the symlink rather than the target. Consult the docs for `chmod()` for the possible values of *mode*. Since Python 3.3, this matches `os.chmod(path, mode, follow_symlinks=False)`.

`lchmod()` is not part of POSIX, yet Unix implementations may offer it where changing the mode of symbolic links is supported.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chmod` with arguments `path`, `mode`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not Linux, FreeBSD >= 1.3, NetBSD >= 1.3, not OpenBSD

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.13: Added support on Windows.

 os.lchown(*path*, *uid*, *gid*)

Reassign the owning user and group of *path* to the numeric *uid* and *gid*. Symbolic links are never followed by this function. Since Python 3.3, this matches `os.chown(path, uid, gid, follow_symlinks=False)`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](chmod-windows-permission-limits.md) · [Continue](os-link-to-os-listvolumes.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
