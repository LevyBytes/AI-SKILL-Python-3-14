# os: `os.mknod()`, `os.major()`, `os.minor()`, `os.makedev()`, `os.pathconf()`, `os.pathconf_names`, `os.readlink()`

os.mknod(*path*, *mode=0o600*, *device=0*, ***, *dir_fd=None*)

Build a filesystem node (a file, a device special file, or a named pipe) called *path*. *mode* sets both the permissions to use and the node kind being built, OR-combined bitwise with one of `stat.S_IFREG`, `stat.S_IFCHR`, `stat.S_IFBLK`, and `stat.S_IFIFO` (those constants live in [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat)). For `stat.S_IFCHR` and `stat.S_IFBLK`, *device* declares the freshly created device special file (likely via `os.makedev()`); otherwise it is disregarded.

This function can also support paths relative to directory descriptors.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

Changed in version 3.3: Added the *dir_fd* parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.major(*device*, */*)

Pull the device major number out of a raw device number (usually the `st_dev` or `st_rdev` field from `stat`).

 os.minor(*device*, */*)

Pull the device minor number out of a raw device number (usually the `st_dev` or `st_rdev` field from `stat`).

 os.makedev(*major*, *minor*, */*)

Assemble a raw device number from the major and minor device numbers.

 os.pathconf(*path*, *name*)

Give back system configuration information that pertains to a named file. *name* declares which configuration value to fetch; it may be a string giving the name of a defined system value; such names are laid out across several standards (POSIX.1, Unix 95, Unix 98, and more). Certain platforms define extra names as well. The names recognized by the host operating system are listed in the `pathconf_names` dictionary. For configuration variables absent from that mapping, passing an integer for *name* is also accepted.

When *name* is a string and is not recognized, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Should the host system not support a particular value for *name*, even when it does appear in `pathconf_names`, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised with [`errno.EINVAL`](https://docs.python.org/3.14/library/errno.html#errno.EINVAL) for the error number.

This function can support specifying a file descriptor.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.pathconf_names

Dictionary that maps the names accepted by `pathconf()` and `fpathconf()` to the integer values the host operating system defines for those names. This can serve to determine the set of names the system recognizes.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

 os.readlink(*path*, ***, *dir_fd=None*)

Give back a string holding the path that the symbolic link points to. The result may come back either as an absolute or a relative pathname; when it is relative, it may be turned into an absolute pathname with `os.path.join(os.path.dirname(path), result)`.

[Subject index](INDEX.md) · [Previous](os-lstat-to-os-mkfifo.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Required continuation of the source contract](os-remove-to-os-renames.md)
