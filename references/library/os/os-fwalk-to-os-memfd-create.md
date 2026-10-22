# os: `os.fwalk()`, `os.memfd_create()`

os.fwalk(*top='.'*, *topdown=True*, *onerror=None*, ***, *follow_symlinks=False*, *dir_fd=None*)

This acts exactly like `walk()`, except that it yields a 4-tuple `(dirpath, dirnames, filenames, dirfd)`, and it supports `dir_fd`.

*dirpath*, *dirnames* and *filenames* match the `walk()` output, and *dirfd* is a file descriptor referring to the directory *dirpath*.

Paths relative to directory descriptors plus skipping symlink resolution are always supported by this function. Be aware, though, that unlike other functions, `fwalk()` defaults *follow_symlinks* to `False`.

Note

Since `fwalk()` yields file descriptors, each one remains valid only through the next iteration step, so duplicate them (for example with `dup()`) whenever you want to keep them around longer.

For every directory beneath the starting directory, this example reports how many bytes the non-directory files take up, while steering clear of any `__pycache__` subdirectory:

```python
import os
for root, dirs, files, rootfd in os.fwalk('python/Lib/xml'):
    print(root, "consumes", end=" ")
    print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
          end=" ")
    print("bytes in", len(files), "non-directory files")
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')  # don't visit __pycache__ directories

```

In the next example, a bottom-up traversal of the tree is crucial: `rmdir()` refuses to delete a directory until that directory has been emptied:

```python
# Delete everything reachable from the directory named in "top",
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
for root, dirs, files, rootfd in os.fwalk(top, topdown=False):
    for name in files:
        os.unlink(name, dir_fd=rootfd)
    for name in dirs:
        os.rmdir(name, dir_fd=rootfd)

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.fwalk` with arguments `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.3.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.7: Added support for [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) paths.

 os.memfd_create(*name*[, *flags=os.MFD_CLOEXEC*])

Create an anonymous file and give back a file descriptor that refers to it. For *flags* you supply one of the `os.MFD_*` constants the system provides (or a bitwise ORed combination of them). The freshly made file descriptor defaults to non-inheritable.

The name supplied in *name* serves as a filename and gets shown as the target of the matching symbolic link in the directory `/proc/self/fd/`. The shown name always carries the prefix `memfd:` and serves debugging purposes only. Names have no bearing on the behavior of the file descriptor, and so several files can carry the same name without any side effects.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Linux >= 3.17 with glibc >= 2.27.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](os-walk.md) · [Continue](os-mfd-cloexec-to-os-eventfd.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md)
