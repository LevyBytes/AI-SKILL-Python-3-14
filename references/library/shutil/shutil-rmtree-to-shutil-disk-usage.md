# shutil: `shutil.rmtree()`, `rmtree.avoids_symlink_attacks`, `shutil.move()`, `shutil.disk_usage()`

shutil.rmtree(*path*, *ignore_errors=False*, *onerror=None*, ***, *onexc=None*, *dir_fd=None*)

Remove a whole directory tree; *path* has to name a directory (and not a symbolic link to a directory). When *ignore_errors* is true, any errors stemming from failed removals are disregarded; when false or left out, such errors get routed to a handler named by *onexc* or *onerror*, or — if both are left out — the exceptions propagate up to the caller.

This function is able to support [paths relative to directory descriptors](https://docs.python.org/3.14/library/os.html#dir-fd).

Note

On platforms providing the needed fd-based functions, a symlink-attack-resistant variant of `rmtree()` runs by default. Elsewhere, the `rmtree()` implementation can fall prey to a symlink attack: with the right timing and conditions, attackers can tamper with symlinks on the filesystem to erase files they otherwise could not reach. Applications can check the `rmtree.avoids_symlink_attacks` function attribute to learn which scenario is in play.

When *onexc* is supplied, it has to be a callable accepting three parameters: *function*, *path*, and *excinfo*.

The first parameter, *function*, is whichever function threw the exception; which one it is varies by platform and implementation. The second parameter, *path*, holds the path name that was handed to *function*. The third parameter, *excinfo*, carries the exception that got thrown. Any exception thrown by *onexc* goes uncaught.

The deprecated *onerror* resembles *onexc*, save that the third parameter it gets is the tuple returned from [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info).

See also

rmtree example, which demonstrates how to deal with deleting a directory tree holding read-only files.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.rmtree` with arguments `path`, `dir_fd`.

Changed in version 3.3: A symlink-attack-resistant variant was introduced, applied automatically wherever the platform offers fd-based functions.

Changed in version 3.8: Under Windows, the contents of a directory junction are no longer erased ahead of removing the junction itself.

Changed in version 3.11: The *dir_fd* parameter was introduced.

Changed in version 3.12: The *onexc* parameter was introduced, and *onerror* was deprecated.

Changed in version 3.13: For every path other than the top-level one, `rmtree()` now disregards [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) exceptions. Anything that is neither an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) nor a subclass of `OSError` is now invariably propagated to the caller.

 rmtree.avoids_symlink_attacks

Reports whether the current platform and implementation supply a symlink-attack-resistant variant of `rmtree()`. At present this holds true only for platforms that offer fd-based directory access functions.

Added in version 3.3.

 shutil.move(*src*, *dst*, *copy_function=copy2*)

Recursively relocate a file or directory (*src*) to a different location, returning the destination.

Whenever *dst* names an existing directory, or a symlink pointing at one, *src* gets moved into that directory. Within it, the destination path has to be absent beforehand.

When *dst* already exists yet is not a directory, it may get overwritten subject to [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename) semantics.

Internally, [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename) is the preferred mechanism whenever *src* and the destination sit on the same filesystem. Should `os.rename()` fail with an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) (for instance, where the user holds write permission on the destination file yet lacks it on the enclosing parent directory), the method resorts to *copy_function*; under that path *src* is reproduced at the destination via *copy_function* and afterwards removed.

For symlinks, a brand-new symlink targeting the original *src* target is created in or as the destination, and *src* is removed.

When *copy_function* is supplied, it has to be a callable taking two arguments, *src* and the destination, and it serves to copy *src* to the destination whenever [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename) cannot be applied. When the source is a directory, `copytree()` runs, with the *copy_function* handed to it. The default *copy_function* is `copy2()`. Choosing `copy()` as the *copy_function* lets the move go through in cases where copying the metadata as well is impossible, at the cost of copying none of the metadata.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.move` with arguments `src`, `dst`.

Changed in version 3.3: Explicit symlink handling for foreign filesystems was introduced, aligning it with the behavior of GNU's **mv**. The return value is now *dst*.

Changed in version 3.5: The *copy_function* keyword argument was introduced.

Changed in version 3.8: To copy a file with greater efficiency, the routine may internally call fast-copy syscalls that are specific to the platform. Refer to the Platform-dependent efficient copy operations section.

Changed in version 3.9: A [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) is now accepted for both *src* and *dst*.

 shutil.disk_usage(*path*)

Report disk usage figures for the supplied path as a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying the attributes *total*, *used* and *free*, which give the total, used, and free space, in bytes. The value *path* may be a file or a directory.

Note

On Unix filesystems, *path* has to point at a path inside a **mounted** filesystem partition. On those platforms, CPython makes no attempt to fetch disk usage data from non-mounted filesystems.

Added in version 3.3.

Changed in version 3.8: Under Windows, *path* is now allowed to be a file or a directory.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

[Subject index](INDEX.md) · [Previous](shutil-copy-to-shutil-copytree.md) · [Continue](shutil-chown-to-shutil-error.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Owning module, declaration or section: Directory and files operations](shutil-copyfileobj-to-shutil-copystat.md)
