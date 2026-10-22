# Python 3.13.0 alpha 3 / library / shutil

[bpo-26791](https://bugs.python.org/issue?@action=redirect&bpo=26791): When the destination directory is the very target of a symlink, [`shutil.move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) now relocates that symlink into the directory, mirroring how the mv shell command behaves. Previously such a case raised an exception. Jeffrey Kintscher wrote the patch.

[gh-113188](https://github.com/python/cpython/issues/113188): Repair [`shutil.copymode()`](https://docs.python.org/3.14/library/shutil.html#shutil.copymode) plus [`shutil.copystat()`](https://docs.python.org/3.14/library/shutil.html#shutil.copystat) on Windows. Their old behavior diverged whenever *dst* was a symbolic link: when *follow_symlinks* was true or *src* was not itself a symbolic link, they altered the permission bits on *dst* directly instead of those of its target, and they left the permission bits untouched when *follow_symlinks* was false while *src* was a symbolic link.

[gh-94692](https://github.com/python/cpython/issues/94692): Only OSError exceptions are now caught by [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree). Formerly, the symlink-attack-resistant variant of `shutil.rmtree()` might swallow, or route to the error handler, an arbitrary exception raised when bad arguments were supplied.

[gh-112645](https://github.com/python/cpython/issues/112645): Drop the deprecation error triggered by handing `onerror` to [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree).

[bpo-37260](https://bugs.python.org/issue?@action=redirect&bpo=37260): Resolved a timing hazard in [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree): when a separate process or thread deletes directory entries while `shutil.rmtree()` runs, the call could surface FileNotFoundError. Jeffrey Kintscher supplied the patch.

[bpo-35332](https://bugs.python.org/issue?@action=redirect&bpo=35332): When *ignore_errors* is `True`, the [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) function now disregards errors from calling [`os.close()`](https://docs.python.org/3.14/library/os.html#os.close), and `os.close()` is no longer retried following an error.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
