# Python 3.9.0 alpha 1 / library / files and paths

[bpo-37520](https://bugs.python.org/issue?@action=redirect&bpo=37520): Fixed how zipfile.Path.parent behaves once the path object points at a subdirectory.

[bpo-37421](https://bugs.python.org/issue?@action=redirect&bpo=37421): Adjusted the `multiprocessing.util.get_temp_dir()` finalizer to additionally wipe the current process's ?tempdir? configuration; that way the next `get_temp_dir()` call builds a fresh temporary directory rather than recycling the one already deleted.

[bpo-37280](https://bugs.python.org/issue?@action=redirect&bpo=37280): The sendfile fallback mode now reads from file by way of a threadpool.

[bpo-31163](https://bugs.python.org/issue?@action=redirect&bpo=31163): The rename and replace methods on a pathlib.Path instance now hand back the new Path instance.

[bpo-37689](https://bugs.python.org/issue?@action=redirect&bpo=37689): A new `is_relative_to()` method on `PurePath` reports whether one path sits relative to another.

[bpo-11122](https://bugs.python.org/issue?@action=redirect&bpo=11122): Distutils stops restricting its rpmbuild lookup to only the supplied paths.

[bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692): Introduced `asyncio.PidfdChildWatcher`, a Linux-only child watcher implementation polling process file descriptors.

[bpo-37772](https://bugs.python.org/issue?@action=redirect&bpo=37772): Inside `zipfile.Path`, when implicit dirs are added, ancestral directories are now guaranteed to be added while duplicates are kept out.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
