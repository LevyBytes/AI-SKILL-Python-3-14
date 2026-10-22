# shutil: `shutil.copy()`, `shutil.copy2()`, `shutil.ignore_patterns()`, `shutil.copytree()`

shutil.copy(*src*, *dst*, ***, *follow_symlinks=True*)

Copy the file *src* onto the file or directory *dst*. Both *src* and *dst* should be [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) or strings. When *dst* names a directory, the file lands inside *dst* under the base filename taken from *src*. When *dst* names a file that already exists, it gets replaced. Returns the path of the file just created.

When *follow_symlinks* is false, and *src* is a symbolic link, *dst* will be made into a symbolic link. When *follow_symlinks* is true and *src* is a symbolic link, *dst* becomes a copy of the file that *src* targets.

`copy()` reproduces the file data plus the file's permission mode (see [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod)). Further metadata, such as the file's creation and modification times, is left out. If you need to keep all file metadata from the source, reach for `copy2()` instead.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copymode` with arguments `src`, `dst`.

Changed in version 3.3: The *follow_symlinks* argument was introduced; the path of the newly created file is now what gets returned.

Changed in version 3.8: To copy a file with greater efficiency, the routine may internally call fast-copy syscalls that are specific to the platform. Refer to the Platform-dependent efficient copy operations section.

 shutil.copy2(*src*, *dst*, ***, *follow_symlinks=True*)

Behaves the same as `copy()`, except that `copy2()` additionally tries to keep file metadata.

When *follow_symlinks* is false, and *src* is a symbolic link, `copy2()` tries to carry all metadata over from the *src* symbolic link onto the freshly made *dst* symbolic link. That capability, however, is not offered on every platform. On platforms where part or all of it is missing, `copy2()` keeps every bit of metadata it can; `copy2()` never throws an exception just because it failed to keep file metadata.

To carry the file metadata over, `copy2()` leans on `copystat()`. For details on which platforms can modify symbolic link metadata, consult `copystat()`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copyfile` with arguments `src`, `dst`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copystat` with arguments `src`, `dst`.

Changed in version 3.3: The *follow_symlinks* argument was introduced, with an added attempt to copy extended file system attributes as well (Linux only for now); the path of the newly created file is now what gets returned.

Changed in version 3.8: To copy a file with greater efficiency, the routine may internally call fast-copy syscalls that are specific to the platform. Refer to the Platform-dependent efficient copy operations section.

 shutil.ignore_patterns(**patterns*)

This factory function builds a function usable as a callable for the *ignore* argument of `copytree()`, skipping any files and directories matching one of the glob-style *patterns* you pass. See the example below.

 shutil.copytree(*src*, *dst*, *symlinks=False*, *ignore=None*, *copy_function=copy2*, *ignore_dangling_symlinks=False*, *dirs_exist_ok=False*)

Recursively copy a whole directory tree rooted at *src* into a directory called *dst*, returning the destination directory. By default, every intermediate directory required to hold *dst* is created as well.

The permissions and times of directories are reproduced with `copystat()`, while individual files are copied via `copy2()`.

When *symlinks* is true, any symbolic link in the source tree appears once more as a symbolic link within the fresh tree, while each original link's metadata is reproduced to whatever degree the platform permits; when false or left out, what gets reproduced into the fresh tree is the contents and metadata of the linked-to files.

If *symlinks* is false and the file the symlink targets does not exist, an entry is appended to the list of errors raised within an `Error` exception once the copy finishes. To suppress that exception, you can set the optional *ignore_dangling_symlinks* flag to true. Note that this option does nothing on platforms lacking [`os.symlink()`](https://docs.python.org/3.14/library/os.html#os.symlink).

When *ignore* is supplied, it has to be a callable that receives as its arguments the directory `copytree()` is currently visiting plus a list of that directory's contents, as produced by [`os.listdir()`](https://docs.python.org/3.14/library/os.html#os.listdir). Because `copytree()` runs recursively, the *ignore* callable fires once per copied directory. What that callable has to hand back is a sequence, relative to the current directory, of file and directory names (in other words, a subset of the entries in its second argument); the copy then skips those names. You can use `ignore_patterns()` to build such a callable that skips names according to glob-style patterns.

Should one or more exceptions occur, an `Error` is raised carrying a list of reasons.

When *copy_function* is supplied, it has to be a callable that copies each file. Its arguments at call time are the source path together with the destination path. By default the function chosen is `copy2()`, yet any function carrying that same signature (such as `copy()`) works.

When *dirs_exist_ok* is false (the default) and *dst* already exists, a [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) is raised. When *dirs_exist_ok* is true, the copy proceeds past any existing directories it runs into, and files inside the *dst* tree are overwritten by the matching files from the *src* tree.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `shutil.copytree` with arguments `src`, `dst`.

Changed in version 3.2: The *copy_function* argument was introduced so that a custom copy function can be supplied. The *ignore_dangling_symlinks* argument was introduced to quiet dangling-symlink errors when *symlinks* is false.

Changed in version 3.3: Metadata is now copied when *symlinks* is false. The return value is now *dst*.

Changed in version 3.8: To copy a file with greater efficiency, the routine may internally call fast-copy syscalls that are specific to the platform. Refer to the Platform-dependent efficient copy operations section.

Changed in version 3.8: The *dirs_exist_ok* parameter was introduced.

[Subject index](INDEX.md) · [Previous](shutil-copyfileobj-to-shutil-copystat.md) · [Continue](shutil-rmtree-to-shutil-disk-usage.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md) · [Owning module, declaration or section: Directory and files operations](shutil-copyfileobj-to-shutil-copystat.md)
