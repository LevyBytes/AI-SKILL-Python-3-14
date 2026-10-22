# os: `os.access()`

### Files and Directories

On certain Unix platforms, a number of these functions provide one or more of the features below:

- **specifying a file descriptor:** Ordinarily the *path* argument handed to functions in the `os` module has to be a string giving a file path. Some functions, however, will now also accept an open file descriptor for their *path* argument. The function then acts on the file that the descriptor references. For POSIX systems, Python invokes the variant of the function carrying an `f` prefix (for instance it calls `fchdir` rather than `chdir`).

You can confirm whether *path* may be given as a file descriptor for a specific function on your platform by checking `os.supports_fd`. Where this capability is missing, using it raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

When the function additionally accepts *dir_fd* or *follow_symlinks* arguments, supplying one of those alongside *path* as a file descriptor is an error.

- **paths relative to directory descriptors:** When *dir_fd* is not `None`, it should be a file descriptor that references a directory, and the path being operated on should be relative; path is then taken relative to that directory. When the path is absolute, *dir_fd* is disregarded. For POSIX systems, Python invokes the variant of the function bearing an `at` suffix and possibly an `f` prefix (for instance it calls `faccessat` rather than `access`).

You can confirm whether *dir_fd* is honored for a specific function on your platform by checking `os.supports_dir_fd`. Where it is missing, using it raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

- **not following symlinks:** When *follow_symlinks* is `False`, and the final component of the path being operated on is a symbolic link, the function acts on the symbolic link itself instead of the file the link points to. For POSIX systems, Python invokes the `l...` variant of the function.

You can confirm whether *follow_symlinks* is honored for a specific function on your platform by checking `os.supports_follow_symlinks`. Where it is missing, using it raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

 os.access(*path*, *mode*, ***, *dir_fd=None*, *effective_ids=False*, *follow_symlinks=True*)

Employ the real uid/gid to check access to *path*. Bear in mind that most operations rely on the effective uid/gid, so this routine can serve in a suid/sgid environment to verify whether the invoking user holds the named access to *path*. *mode* should be `F_OK` to check that *path* exists, or it may be the inclusive OR of one or more of `R_OK`, `W_OK`, and `X_OK` to check permissions. Returns [`True`](https://docs.python.org/3.14/library/constants.html#True) when access is granted, [`False`](https://docs.python.org/3.14/library/constants.html#False) when it is not. Consult the Unix man page *[access(2)](https://manpages.debian.org/access(2))* for further detail.

Support exists for giving paths relative to directory descriptors and for skipping symlink resolution.

[Subject index](INDEX.md) · [Previous](os-get-inheritable-to-os-set-handle-inheritable.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Required continuation of the source contract](os-f-ok-to-os-chdir.md)
