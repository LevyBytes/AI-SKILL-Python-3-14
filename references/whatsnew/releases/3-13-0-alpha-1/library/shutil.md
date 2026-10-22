# Python 3.13.0 alpha 1 / library / shutil

[gh-99203](https://github.com/python/cpython/issues/99203): Brought back the CPython <= 3.10.5 conduct of [`shutil.make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive): refrain from producing an empty archive when `root_dir` is not a directory, and under that condition raise [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) or [`NotADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#NotADirectoryError) no matter the `format` selected. Past that restored conduct, the function can now raise those same exceptions during `dry_run` mode too.

[gh-109590](https://github.com/python/cpython/issues/109590): On win32, [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) will favor files carrying an extension listed in `PATHEXT` whenever the supplied mode contains `os.X_OK`. When nothing in `PATHEXT` matches, a file lacking a `PATHEXT` extension may still be returned. With this adjustment, [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) behaves closer to how it did back in Python 3.11.

[gh-83006](https://github.com/python/cpython/issues/83006): Record how [`shutil.disk_usage()`](https://docs.python.org/3.14/library/shutil.html#shutil.disk_usage) behaves for filesystems that are not mounted on Unix.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
