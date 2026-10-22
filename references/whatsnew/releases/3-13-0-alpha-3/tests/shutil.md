# Python 3.13.0 alpha 3 / tests / shutil

[gh-109980](https://github.com/python/cpython/issues/109980): Repair `test_tarfile_vs_tar` in `test_shutil` on macOS, where the system tar may embed extra archive data beyond what [`shutil.make_archive`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) writes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
