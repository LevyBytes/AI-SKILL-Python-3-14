# os - Linux extended attributes

### Linux extended attributes

Added in version 3.3.

Every one of these functions is available on Linux only.

 os.getxattr(*path*, *attribute*, ***, *follow_symlinks=True*)

Give back what the extended filesystem attribute *attribute* holds for *path*. *attribute* can come as bytes or str (whether directly or through the `PathLike` interface). When it arrives as str, the filesystem encoding is applied to encode it.

Support exists here for giving a file descriptor and for skipping symlink resolution.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.getxattr` with arguments `path`, `attribute`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *path* and *attribute*.

 os.listxattr(*path=None*, ***, *follow_symlinks=True*)

Give back a list of the extended filesystem attributes attached to *path*. Each attribute in that list appears as a string decoded with the filesystem encoding. When *path* is `None`, `listxattr()` will inspect the current directory.

Support exists here for giving a file descriptor and for skipping symlink resolution.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.listxattr` with argument `path`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.removexattr(*path*, *attribute*, ***, *follow_symlinks=True*)

Drops the extended filesystem attribute *attribute* off of *path*. *attribute* should arrive as bytes or str (whether directly or through the `PathLike` interface). When it is a string, the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is applied to encode it.

Support exists here for giving a file descriptor and for skipping symlink resolution.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.removexattr` with arguments `path`, `attribute`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *path* and *attribute*.

 os.setxattr(*path*, *attribute*, *value*, *flags=0*, ***, *follow_symlinks=True*)

Assign *value* to the extended filesystem attribute *attribute* on *path*. *attribute* has to be a bytes or str carrying no embedded NULs (whether directly or through the `PathLike` interface). When it arrives as a str, the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) is applied to encode it. *flags* may be `XATTR_REPLACE` or `XATTR_CREATE`. When `XATTR_REPLACE` is given while the attribute is missing, `ENODATA` will be raised. When `XATTR_CREATE` is given while the attribute is already present, the attribute is left uncreated and `EEXISTS` will be raised.

Support exists here for giving a file descriptor and for skipping symlink resolution.

Note

On certain filesystems, a bug present in Linux kernel versions below 2.6.39 led the flags argument to be ignored.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.setxattr` with arguments `path`, `attribute`, `value`, `flags`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *path* and *attribute*.

 os.XATTR_SIZE_MAX

The largest size the value of an extended attribute can reach. For now, this is 64 KiB on Linux.

 os.XATTR_CREATE

This is a possible value for the flags argument in `setxattr()`. It signals that the operation has to create an attribute.

 os.XATTR_REPLACE

This is a possible value for the flags argument in `setxattr()`. It signals that the operation has to replace an existing attribute.

[Subject index](INDEX.md) · [Previous](os-tfd-cloexec-to-os-tfd-timer-cancel-on-set.md) · [Continue](os-abort-to-os-ex-ok.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
