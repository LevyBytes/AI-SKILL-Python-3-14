# os: `os.statvfs()`, `os.supports_dir_fd`, `os.supports_effective_ids`, `os.supports_fd`, `os.supports_follow_symlinks`

os.statvfs(*path*)

Carry out a `statvfs()` system call against the supplied path. What comes back is an object whose attributes characterize the filesystem at that path, lining up with the members of the `statvfs` structure, namely: `f_bsize`, `f_frsize`, `f_blocks`, `f_bfree`, `f_bavail`, `f_files`, `f_ffree`, `f_favail`, `f_flag`, `f_namemax`, `f_fsid`.

Two module-level constants exist for the bit-flags of the `f_flag` attribute: when `ST_RDONLY` is set, the filesystem is mounted read-only, and when `ST_NOSUID` is set, the semantics of setuid/setgid bits are disabled or unsupported.

GNU/glibc based systems define further module-level constants. They are `ST_NODEV` (block access to device special files), `ST_NOEXEC` (block program execution), `ST_SYNCHRONOUS` (writes get synced immediately), `ST_MANDLOCK` (permit mandatory locks on a filesystem), `ST_WRITE` (writable file, directory, or symlink), `ST_APPEND` (file that only appends), `ST_IMMUTABLE` (file that cannot change), `ST_NOATIME` (skip updating access times), `ST_NODIRATIME` (skip updating directory access times), `ST_RELATIME` (refresh atime against mtime/ctime).

This function can support specifying a file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.2: The `ST_RDONLY` and `ST_NOSUID` constants were added.

Changed in version 3.3: Giving *path* as an open file descriptor is now supported.

Changed in version 3.4: The `ST_NODEV`, `ST_NOEXEC`, `ST_SYNCHRONOUS`, `ST_MANDLOCK`, `ST_WRITE`, `ST_APPEND`, `ST_IMMUTABLE`, `ST_NOATIME`, `ST_NODIRATIME`, and `ST_RELATIME` constants were added.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: Added the `f_fsid` attribute.

 os.supports_dir_fd

A [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) object marking which functions in the `os` module take an open file descriptor for their *dir_fd* parameter. Platforms differ in what they provide, and the underlying functionality Python relies on to implement the *dir_fd* parameter is absent on some of the platforms Python supports. For the sake of consistency, functions that may support *dir_fd* always let you name the parameter, but raise an exception when the functionality gets used where it is not locally available. (Naming `None` for *dir_fd* is always supported on every platform.)

To check whether a particular function takes an open file descriptor for its *dir_fd* parameter, apply the `in` operator to `supports_dir_fd`. For instance, this expression evaluates to `True` when `os.stat()` takes open file descriptors for *dir_fd* on the local platform:

```python
os.stat in os.supports_dir_fd

```

For now, *dir_fd* parameters work only on Unix platforms; none of them work on Windows.

Added in version 3.3.

 os.supports_effective_ids

A [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) object marking whether `os.access()` allows naming `True` for its *effective_ids* parameter on the local platform. (Naming `False` for *effective_ids* is always supported on every platform.) When the local platform supports it, the collection holds `os.access()`; otherwise it is empty.

This expression evaluates to `True` when `os.access()` supports `effective_ids=True` on the local platform:

```python
os.access in os.supports_effective_ids

```

For now, *effective_ids* is supported only on Unix platforms; it does not work on Windows.

Added in version 3.3.

 os.supports_fd

A [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) object marking which functions in the `os` module allow naming their *path* parameter as an open file descriptor on the local platform. Platforms differ in what they provide, and the underlying functionality Python relies on to take open file descriptors as *path* arguments is absent on some of the platforms Python supports.

To determine whether a particular function allows naming an open file descriptor for its *path* parameter, apply the `in` operator to `supports_fd`. For instance, this expression evaluates to `True` when `os.chdir()` takes open file descriptors for *path* on your local platform:

```python
os.chdir in os.supports_fd

```

Added in version 3.3.

 os.supports_follow_symlinks

A [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) object marking which functions in the `os` module take `False` for their *follow_symlinks* parameter on the local platform. Platforms differ in what they provide, and the underlying functionality Python relies on to implement *follow_symlinks* is absent on some of the platforms Python supports. For the sake of consistency, functions that may support *follow_symlinks* always let you name the parameter, but raise an exception when the functionality gets used where it is not locally available. (Naming `True` for *follow_symlinks* is always supported on every platform.)

To check whether a particular function takes `False` for its *follow_symlinks* parameter, apply the `in` operator to `supports_follow_symlinks`. For instance, this expression evaluates to `True` when you may name `follow_symlinks=False` while calling `os.stat()` on the local platform:

```python
os.stat in os.supports_follow_symlinks

```

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](stat-macos-and-windows-fields.md) · [Continue](os-symlink-to-os-unlink.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
